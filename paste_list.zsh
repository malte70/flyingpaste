#!/bin/zsh

cd $(dirname $0)

#SQL_QUERY='SELECT id,title,language,author_name FROM pastes WHERE privacy=0;'
SQL_QUERY='
SELECT
	`title` AS `NoPaste Title`,
	CONCAT( "https://nopaste.rt3x.de/p/" , `id` , ".html" ) AS `NoPaste URL`,
	`language` AS `Language Code`,
	CONCAT( `author_name` , " <" , `author_email` , ">" ) AS `Author`,
	`date_added` AS `Added`
FROM
	`pastes`
WHERE
	`privacy` = 0;
'

#FLYINGPASTE_USER=$(grep ^CONFIG_MYSQL_USER= flyingpaste.py | cut -d\" -f2)
#FLYINGPASTE_PASSWORD=$(grep ^CONFIG_MYSQL_PASSWORD= flyingpaste.py | cut -d\" -f2)
#FLYINGPASTE_DB=$(grep ^CONFIG_MYSQL_DB= flyingpaste.py | cut -d\" -f2)
FLYINGPASTE_USER=$(python3 -c 'import configparser;cfg=configparser.ConfigParser();cfg.read("flyingpaste.ini");print(cfg.get("DATABASE","MYSQL_USER"))')
FLYINGPASTE_PASSWORD=$(python3 -c 'import configparser;cfg=configparser.ConfigParser();cfg.read("flyingpaste.ini");print(cfg.get("DATABASE","MYSQL_PASSWORD"))')
FLYINGPASTE_DB=$(python3 -c 'import configparser;cfg=configparser.ConfigParser();cfg.read("flyingpaste.ini");print(cfg.get("DATABASE","MYSQL_DB"))')

mysql \
	-e "${SQL_QUERY}"            \
	-u "${FLYINGPASTE_USER}"     \
	-p"${FLYINGPASTE_PASSWORD}"  \
	"${FLYINGPASTE_DB}"          \
	2>/dev/null

