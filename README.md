Flying Paste
============

What's this
-----------

Flying Paste is a Nopaste application based on Python featuring
syntax highlighting and full database storage (no write access to
any file required).

Requirements
------------

 - Python 2
 - bottle
 - Pygments
 - Python-MySQL
 - a running MySQL server

Installation
------------

 - get the latest code from github with:
      git clone https://github.com/malte70/flyingpaste
 - Optional: create a special database user for the application
 - create a table using the following SQL statement:
   ```sql
   CREATE TABLE pastes (
      id VARCHAR(20) PRIMARY KEY,
      title VARCHAR(200) DEFAULT "Untitled",
      description TEXT DEFAULT NULL,
      author_name VARCHAR(50) DEFAULT "Anonymous",
      author_email VARCHAR(50) DEFAULT NULL,
      code TEXT NOT NULL,
      language VARCHAR(20) DEFAULT "text",
      privacy VARCHAR(20) DEFAULT "public"
   )```
 - edit the database settings in the executable (flyingpaste.py)

Running
-------

### Run directly in testing mode
simple execute the flyingpaste.py from the command line:

   cd /path/to/flyingpaste
   python2 flyingpaste.py

Please note that you have to be in the directory containing the \*.tpl-files,
otherwise, Flying Paste wouldn't be able to find them.

Homepage and source code repository
-----------------------------------

Available on github: https://github.com/malte70/flyingpaste
No website at the moment (there will be one later)

Contacting the author
---------------------

If you have wished or just want to contact me,
write me an EMail to

    me@malte-bublitz.de

You can find my GPG key here (I prefer encrypted mails):
http://malte70.de/gpg-key.asc
or here:
ftp://ftp.malte-bublitz.de/pub/malte70/gpg-key.asc
or here:
gopher://flying-sheep.de/0/malte70/contact.txt

Licensing
---------

Flying Paste is free/libre software released under the 2-clause BSD license
(also known as the "Simplified BSD license" or "FreeBSD license"), which
can be found in the file COPYING.md.

Submitting bugs/feature requests
--------------------------------

If you have found a bug or like to see a specific feature, open an issue on
github (https://github.com/malte70/flyingpaste/issues/new) or leave me an
EMail (see "Contacting the author").

