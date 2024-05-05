Flying Paste
============

What's this
-----------

Flying Paste is a Nopaste application based on Python featuring
syntax highlighting and full database storage (no write access to
any file required).

Requirements
------------

 - Python 3
 - bottle
 - Pygments
 - Python-MySQL
 - a running MySQL server

Installation
------------

- Get the latest code from github with:
  ```sh
  git clone https://github.com/malte70/flyingpaste
  ```
- Optional: create a special database user for the application
- Create a table using the following SQL statement:
  ```sql
  CREATE TABLE pastes (
  	id VARCHAR(20) NOT NULL PRIMARY KEY,
  	title VARCHAR(200) DEFAULT "Untitled",
  	description TEXT DEFAULT NULL,
  	author_name VARCHAR(50) DEFAULT "Anonymous",
  	author_email VARCHAR(50) DEFAULT NULL,
  	code TEXT NOT NULL,
  	language VARCHAR(20) DEFAULT "text",
  	privacy VARCHAR(20) DEFAULT "public",
	date_added datetime NOT NULL DEFAULT current_timestamp()
  ) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
  ```
- Generate a configuration using the `configure` script:
  ```sh
  cd flyingpaste
  ./configure
  ```

Running
-------

### Run directly in testing mode
Simply execute `flyingpaste.py` from the command line:

```sh
cd /path/to/flyingpaste
python flyingpaste.py
```

### Run using Apache's mod_wsgi

A sample configuration is included in the source as `doc/apache-example.conf`.
Modify it for your needs, activate mod_wsgi and restart your Apache server.
You're done!

Homepage and source code repository
-----------------------------------

Available on github: https://github.com/malte70/flyingpaste
No website at the moment (there will be one later)

Licensing
---------

Flying Paste is free/libre software released under the 2-clause BSD license
(also known as the "Simplified BSD license" or "FreeBSD license"), which
can be found in the file `LICENSE`.

Submitting bugs/feature requests
--------------------------------

If you have found a bug or like to see a specific feature, open an issue on
github (https://github.com/malte70/flyingpaste/issues/new) or leave me an
EMail (see "Contacting the author").

