#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Flying Paste
#    A very simple paste service, which utilizes bottle.py and pygments.
#



################################################################################
# Add application base path to Python's import path and change the
# current directory to it, so we can access the helper modules and
# other files like templates.
# (Needed for mod_wsgi environments)

import os, sys
APP_PATH = os.path.abspath(os.path.dirname(__file__))
os.chdir(APP_PATH)
sys.path.insert(0, APP_PATH)



##########################################
# Import all we need
# 

# use bottle as web framework
import bottle
# for the random id of a new paste and nl2br
import string, random
# We need time.strftime() to show the current year in the footer
import time
# to escape the code for html output
from html import escape as htmlspecialchars
# pygments for syntax highlighting
from pygments import highlight as pygments_highlight
from pygments.lexers import get_lexer_by_name as pygments_get_lexer_by_name
from pygments.formatters import HtmlFormatter as pygments_HtmlFormatter
# Make URLs in descriptions become real HTML links
import re
# Utility functions
from flying_util import LANGUAGES
from flying_util import generate_new_paste_id
from flying_util import nl2br
from flying_util import linkify
from flying_util import file_get_contents
# Configuration handling
import configparser
# MySQLdb
try:
	import MySQLdb
except ImportError:
	print("Error: Module MySQLdb could not be imported, and currently there are no other supported database access methods!", file=sys.stderr)
	sys.exit(1)
# Supress Warnings
#  -> https://stackoverflow.com/a/22408506
import warnings
#warnings.filterwarnings("ignore", category = MySQLdb.Warning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

#DEBUGGING
from pprint import pprint



################################################################################
# Awesome business logic starts here
# 

# Parse .ini configuration
config = configparser.ConfigParser()
config.read(
	os.environ.get(
		"FLYINGPASTE_INI",
		"flyingpaste.ini"
	)
)

assets_path = os.path.join(config.get("APP", "OWNDIR"), "assets")

# debugging if not in productive use.
bottle.debug(not config.getboolean("APP", "PRODUCTIVE"))
#bottle.debug(True)

# Now the magic begins. Or something like that...
pasteapp = bottle.Bottle()

"""
# set up database connection
if config.get("DATABASE", "TYPE") == "MySQL":
	import MySQLdb #import here, so later, when more Database backends are used, the user only needs the used backend to be installed.
	# the actual connection is made when needed, to avoid long-running connections.
else:
	print("Only MySQL is supported as a database backend at the moment. Support for SQLite and flat-file will be added soon.")
	sys.exit(1)
"""


MYSQL_CHARACTER_SET = "utf8mb4"
#MYSQL_CHARACTER_SET = "utf8"

def get_mysql_db_curs():
	db = MySQLdb.connect(
		host   = config.get("DATABASE", "MYSQL_HOST"),
		user   = config.get("DATABASE", "MYSQL_USER"),
		passwd = config.get("DATABASE", "MYSQL_PASSWORD"),
		db     = config.get("DATABASE", "MYSQL_DB"),

	)
	db.set_character_set(MYSQL_CHARACTER_SET)
	
	db_curs = db.cursor()
	db_curs.execute('SET NAMES '+MYSQL_CHARACTER_SET+';')
	db_curs.execute('SET CHARACTER SET '+MYSQL_CHARACTER_SET+';')
	db_curs.execute('SET character_set_connection='+MYSQL_CHARACTER_SET+';')
	
	return [db, db_curs]
	

################################################################################
# Home page
# 
@pasteapp.route("/")
def home():
	if not config.getboolean("APP", "PRODUCTIVE"):
		print(" {:4}  \"/\" -> 200".format(bottle.request.method))
	db, db_curs = get_mysql_db_curs()
	#db_curs.execute('SELECT `id`,`title`,`language`,`author_name` FROM `pastes` WHERE `privacy`="public" ORDER BY `date_added` DESC LIMIT 0,10;')
	db_curs.execute('SELECT `id`,`title`,`language`,`author_name` FROM `pastes` WHERE `privacy`="public" ORDER BY `date_added` DESC;')
	pastes_res = db_curs.fetchall()
	
	pastes = []
	for paste in pastes_res:
		p = {
			"id":       paste[0],
			"title":    paste[1],
			"language": paste[2],
			"author":   paste[3]
		}
		pastes.append(p)
	db.close()
	
	return bottle.template(
		"home",
		title     = config.get("APP","SERVICE_NAME"),
		pastes    = pastes,
		languages = LANGUAGES,
		year      = time.strftime("%Y")
	)



################################################################################
# Show a raw paste
# 
@pasteapp.route("/p/:pasteid#[a-z0-9-_]+#")
def show_paste_plain(pasteid=None):
	if pasteid == None:
		if not config.getboolean("APP", "PRODUCTIVE"):
			print(" {:4}  \"/p/<pasteid>\"  pasteid=\"{}\" => 404 !".format(bottle.request.method, pasteid))
		bottle.abort(404)
	else:
		# check if paste is available
		# TODO: make this portable using an extra abstraction layer so it is transparent to
		# other database backends
		db, db_curs = get_mysql_db_curs()
		db_curs.execute("SELECT code,privacy FROM pastes WHERE id=%s", (pasteid,))
		db.close()
		paste = db_curs.fetchall()
		
		if len(paste) == 0:
			bottle.abort(404, "No paste with id "+str(pasteid)+" found!")
			
		paste = paste[0]
		paste_code = paste[0]
		paste_privacy = paste[1]
		bottle.response.content_type = 'text/plain; charset=UTF-8'
		if not paste_privacy in ("public", "not_listed"):
			bottle.abort(401, "Access denied. Paste is not public, and access to private pastes is not supported yet.")
		return paste_code



################################################################################
# Show a paste in a web site
# 
@pasteapp.route("/p/:pasteid#[a-z0-9-_]+#.html")
def show_paste_html(pasteid=None):
	if pasteid == None:
		if not config.getboolean("APP", "PRODUCTIVE"):
			print(" {:4}  \"/p/<pasteid>\"  pasteid=\"{}\" => 404 !".format(bottle.request.method, pasteid))
		
		bottle.abort(404)
	else:
		if not config.getboolean("APP", "PRODUCTIVE"):
			print(" {:4}  \"/p/<pasteid>\"  pasteid=\"{}\"".format(bottle.request.method, pasteid))
		db, db_curs = get_mysql_db_curs()
		db_curs.execute("SELECT title,description,author_name,author_email,code,language,privacy FROM pastes WHERE id=%s", (pasteid,))
		paste = db_curs.fetchall()
		#paste = db_curs.fetchall()
		if len(paste) == 0:
			bottle.abort(404, "No paste with id "+str(pasteid)+" found!")
		paste = paste[0]
		db.close()
		
		paste_title = paste[0]
		paste_description = linkify(nl2br(htmlspecialchars(paste[1])))
		paste_author_name = paste[2]
		paste_author_email = paste[3]
		paste_code = paste[4]
		paste_language = LANGUAGES[paste[5]]
		paste_privacy = paste[6]
		lexer = pygments_get_lexer_by_name(paste[5], stripall=True, encoding="UTF-8")
		formatter = pygments_HtmlFormatter(linenos=True, cssclass="source", encoding="UTF-8")
		paste_code = pygments_highlight(paste_code, lexer, formatter)
		
		bottle.response.content_type = 'text/html; charset=UTF-8'
		return bottle.template(
			"show_paste",
			service_name = config.get("APP","SERVICE_NAME"),
			title        = paste_title,
			description  = paste_description,
			author_name  = paste_author_name,
			author_email = paste_author_email,
			code         = paste_code,
			language     = paste_language,
			privacy      = paste_privacy,
			year         = time.strftime("%Y")
		)




################################################################################
# Serve CSS files
# 
@pasteapp.route("/assets/css/pygments.css")
def pygments_css():
	formatter = pygments_HtmlFormatter(linenos=True, cssclass="source", encoding="UTF-8")
	bottle.response.content_type = 'text/css; charset=UTF-8'
	return formatter.get_style_defs()
	
#@pasteapp.route("/assets/css/<filename:re:.*\.css")
@pasteapp.route("/assets/css/:filename#.*\.css#")
def assets_css(filename):
	return bottle.static_file(filename, root='assets/css/')
	



################################################################################
# Serve image assets
# 
#@pasteapp.route("/assets/img/<filename:re:.*\.png")
@pasteapp.route("/assets/img/:filename#.*\.png#")
def assets_png(filename):
	#print("assets_png("+filename+")")
	return bottle.static_file(filename, root='assets/img/')
	



################################################################################
# Add a new paste
# 
@pasteapp.route("/add", method="POST")
def add_paste():
	if not config.getboolean("APP", "PRODUCTIVE"):
		print(" {:4}  \"/\" -> 200".format(bottle.request.method))
	
	paste_id           = generate_new_paste_id()
	paste_title        = bottle.request.forms.getunicode("title")
	paste_description  = bottle.request.forms.getunicode("description").replace("\r\n", "\n")
	paste_author_name  = bottle.request.forms.getunicode("author_name")
	paste_author_email = bottle.request.forms.getunicode("author_email")
	paste_code         = bottle.request.forms.getunicode("code").replace("\r\n", "\n")
	paste_lang         = bottle.request.forms.getunicode("language")
	paste_privacy      = bottle.request.forms.getunicode("privacy")
	if not paste_privacy in ("public", "not_listed"):
		bottle.abort(403, "You are trying something evil. Stop it. \""+paste_privacy+"\"")
	
	db, db_curs = get_mysql_db_curs()
	db_curs.execute(
		'INSERT INTO pastes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP());',
		(
			paste_id,
			paste_title,
			paste_description,
			paste_author_name,
			paste_author_email,
			paste_code,
			paste_lang,
			paste_privacy
		)
	)
	
	db.commit()
	db.close()
	bottle.redirect("/p/"+paste_id+".html")




################################################################################
# Support both development setups and productive WSGI environments
# using APP.PRODUCTIVE configuration option
# 
if config.getboolean("APP", "PRODUCTIVE"):
	application = pasteapp
	#print("Running Flying-Paste in WSGI mode.", file=sys.stderr)
	
else:
	pasteapp.run(host="localhost", port=8080)
	
