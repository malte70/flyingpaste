#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Flying Paste
#    A very simple paste service, which utilizes bottle.py and pygments.
#
# Copyright (c) 2013 Malte Bublitz, https://malte-bublitz.de
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#

# configuration
CONFIG_OWNDIR="/usr/share/flyingpaste"             # Where is flying paste installed (i.e. where are the templates etc.)
CONFIG_MYSQL_HOST="localhost"                      # MySQL host
CONFIG_MYSQL_USER="flyingpaste"                    #   "   user
CONFIG_MYSQL_PASSWORD=""                           #   "   password
CONFIG_MYSQL_DB="flyingpaste"                      #   "   database name
CONFIG_DB="MySQL"                                  # database (only MySQL supported at the moment)
CONFIG_SERVICE_URL="http://paste.flying-sheep.de/" # Where will the paste service be available to the public?
CONFIG_SERVICE_NAME="Flying Sheep Paste"           # Name of the paste service (used in document titles)
CONFIG_PRODUCTIVE=False                            # Wether started for testing or productive use. WSGI is used if True.
# configuration end

# NOTE: Database layout
# TODO: Put this in an extra file/make a documentation!
# Table pastes:
#    id           string The id used in the URL
#    title        string The title, used if displayed as a web site
#    description  text   Description of the paste, if a title is not enough
#    author_name  string The name/pseudonym of the uploader, default is "Anonymous"
#    author_email string The EMail adress of the author, used for gravatar in web view
#    code         text   The actual pasted code/text (named code since text is a field type in many
#                        db systems, and because paste services mostly host source code/code snippets
#    language     string The language which will be used to provide syntax highlighting (which will be added soon)
#    privacy      string Privacy setting. Must be either public, not_listed or password: followed
#                        by the password.

# os and sys are always needed
import os,sys
# Change to own directory to access template files
#os.chdir(CONFIG_OWNDIR)
# use bottle as web framework
import bottle
# for the random id of a new paste
import string, random

# debugging. comment out for productive use.
bottle.debug(True)

# Now the magic begins. Or something like that...
pasteapp = bottle.Bottle()

# set up database connection
if CONFIG_DB=="MySQL":
	import MySQLdb #import here, so later, when more Database backends are used, the user only needs the used backend to be installed.
	# the actual connection is made when needed, to avoid long-running connections.
else:
	print "Only MySQL is supported as a database backend at the moment. Support for SQLite and flat-file will be added soon."
	sys.exit(1)

def generate_new_paste_id():
	"""
	generate a random string using lowercase letters and digits
	found here: http://stackoverflow.com/a/2257449/611293
	"""
	size=10
	chars=string.ascii_lowercase + string.digits
	return ''.join(random.choice(chars) for x in range(size))

# home page. static, at the moment.
@pasteapp.route("/")
def home():
	return bottle.template("home", title="Home :: "+CONFIG_SERVICE_NAME)

# show a raw paste
@pasteapp.route("/p/:pasteid#[a-z0-9-_]+#")
def show_paste_plain(pasteid=None):
	if pasteid == None:
		bottle.abort(404)
	else:
		# check if paste is available
		# TODO: make this portable using an extra abstraction layer so it is transparent to
		# other database backends
		db = MySQLdb.connect(
				host=CONFIG_MYSQL_HOST,
				user=CONFIG_MYSQL_USER,
				passwd=CONFIG_MYSQL_PASSWORD,
				db=CONFIG_MYSQL_DB
				)
		db_curs = db.cursor()
		db_curs.execute("SELECT code,privacy FROM pastes WHERE id=\""+MySQLdb.escape_string(pasteid)+"\"")
		db.close()
		paste = db_curs.fetchall()[0]
		paste_code = paste[0]
		paste_privacy = paste[1]
		bottle.response.content_type = 'text/plain; charset=UTF-8'
		if not paste_privacy in ("public", "not_listed"):
			bottle.abort(401, "Access denied. Paste is not public, and access to private pastes is not supported yet.")
		return paste_code

@pasteapp.route("/add", method="POST")
def add_paste():
	paste_id=generate_new_paste_id()
	paste_title=MySQLdb.escape_string(bottle.request.forms.get("title"))
	paste_description=MySQLdb.escape_string(bottle.request.forms.get("description"))
	paste_author_name=MySQLdb.escape_string(bottle.request.forms.get("author_name"))
	paste_author_email=MySQLdb.escape_string(bottle.request.forms.get("author_email"))
	paste_code=MySQLdb.escape_string(bottle.request.forms.get("code"))
	paste_lang=MySQLdb.escape_string(bottle.request.forms.get("language"))
	paste_privacy=MySQLdb.escape_string(bottle.request.forms.get("privacy"))
	if not paste_privacy in ("public", "not_listed"):
		bottle.abort(403, "You are trying something evil. Stop it.")
	db = MySQLdb.connect(
			host=CONFIG_MYSQL_HOST,
			user=CONFIG_MYSQL_USER,
			passwd=CONFIG_MYSQL_PASSWORD,
			db=CONFIG_MYSQL_DB
			)
	db_curs = db.cursor()
	db_curs.execute('INSERT INTO pastes VALUES (\"'+paste_id+'\", \"'+paste_title+'\", \"'+paste_description+'\", \"'+paste_author_name+'\", \"'+paste_author_email+'\", \"'+paste_code+'\", \"'+paste_lang+'\", \"'+paste_privacy+'\");')
	db.commit()
	db.close()
	bottle.redirect("/p/"+paste_id)

if CONFIG_PRODUCTIVE:
	print "Not implemented yet. Sorry."
	sys.exit(1)
else:
	pasteapp.run(host="localhost", port=8080)

