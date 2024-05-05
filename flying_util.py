# -*- coding: utf-8 -*-
# 
# Utility functions and global variables
# 


# os and sys are always needed
import os,sys
# Change to own directory to access template files
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# for the random id of a new paste and nl2br
import string, random
# to escape the code for html output
from html import escape as htmlspecialchars
# Make URLs in descriptions become real HTML links
import re

# Ends at line 93 {{{
LANGUAGES = {
		"text": "Plain text",
		"apacheconf": "Apache Config (.htaccess, apache.conf)",
		"ahk": "AutoHotKey Script",
		"applescript": "AppleScript",
		"arduino": "Arduino",
		"aspx-vb": "ASP.NET (with embedded Visual Basic.NET)",
		"gas": "Assembler (gas)",
		"nasm": "Assembler (NASM)",
		"tasm": "Assembler (TASM)",
		"awk": "Awk",
		"bash": "Bash script",
		"shell-session": "Shell session",
		"bat": "DOS/Windows Batch file",
		"c": "C",
		"cpp": "C++",
		"cbmbas": "CBM BASIC V2",
		"cmake": "CMake",
		"coffee": "CoffeeScript",
		"css": "CSS (Cascading Style Sheet)",
		"diff": "Diff/Patch file",
		"genshi": "Genshi",
		"groff": "Groff",
		"haml": "Haml",
		"hexdump": "Hexdump",
		"html": "HTML (maybe with nested JavaScript and CSS",
		"http": "HTTP",
		"ini": "INI (.ini, .inf, .cfg)",
		"iptables": "iptables",
		"irc": "IRC log (irssi, xchat or weechat style log)",
		"java": "Java",
		"js": "JavaScript",
		"jcl": "JCL",
		"json": "JSON",
		"kconfig": "Kconfig (Linux Kernel Config)",
		"dmesg": "Kernel log (dmesg)",
		"less": "LESS CSS",
		"lighttpd": "Lighttpd config",
		"lua": "Lua",
		"make": "Makefile",
		"mathematica": "Mathematica (.nb, .cdf, .nbp, .ma)",
		"matlab": "Matlab (.m)",
		"md": "Markdown",
		"nginx": "nginx Config",
		"pacmanconf": "pacman.conf",
		"perl": "Perl",
		"perl6": "Perl 6",
		"php": "PHP (pure PHP, without nested HTML)",
		"html+php": "PHP (with nested HTML, JavaScript and CSS)",
		"po": "Gettext Catalog (.po, .pot)",
		"PowerShell": "PowerShell",
		"properties": ".properties",
		"pycon": "Python Console Session",
		"pytb": "Python Traceback",
		"python2": "Python 2",
		"python3": "Python 3",
		"r": "R",
		"rust": "Rust (.rs)",
		"scss": "SCSS",
		"smarty": "Smarty",
		"sourceslist": "Debian sources.list",
		"sql": "SQL",
		"mysql": "SQL (with MySQL extensions)",
		"sqlite": "SQL (SQLite3 console)",
		"tcl": "Tcl",
		"tex": "TeX",
		"todotxt": "todo.txt",
		"typescript": "TypeScript",
		"vb.net": "VisualBasic.NET",
		"vim": "VimL",
		"xml": "XML",
		"xorg.conf": "Xorg.conf",
		"xslt": "XSLT",
		"yaml": "YAML",
}
# }}}

def generate_new_paste_id():
	"""
	generate a random string using lowercase letters and digits
	found here: http://stackoverflow.com/a/2257449/611293
	"""
	size=10
	chars=string.ascii_lowercase + string.digits
	return ''.join(random.choice(chars) for x in range(size))

def nl2br(text, is_xhtml = False):
	"""
	replace every newline with a <br>
	behaves like the PHP function with the same name.
	"""
	return text.replace('\n', '<br>\n') if not is_xhtml else text.replace('\n', '<br />\n')
	
def linkify(text):
	"""
	Replace all URLs in `text` with HTML <a> tags
	"""
	def href(d):
		return '<a href="{}">{}</a>'.format(d,d)
		
	# Source unknown, original implementation used here
	#link_regex = 'https*://.*?(?=[\s$])'
	# https://urlregex.com
	link_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
	# https://stackoverflow.com/a/6883094
	#link_regex = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
	
	return re.sub(link_regex, lambda x:href(x.group()), text)
	
def file_get_contents(filename):
	"""
	Return contents of a file
	"""
	f = open(filename, "r")
	if f:
		contents = f.read()
		f.close()
	else:
		contents = None
	
	return contents
	

