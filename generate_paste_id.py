#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# os and sys are always needed
import os,sys
# Change to own directory to access template files
#os.chdir(CONFIG_OWNDIR)
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# for the random id of a new paste and nl2br
import string, random

#from flyingpaste import generate_new_paste_id
from flying_util import generate_new_paste_id

def _generate_new_paste_id():
	"""
	generate a random string using lowercase letters and digits
	found here: http://stackoverflow.com/a/2257449/611293
	"""
	size=10
	chars=string.ascii_lowercase + string.digits
	return ''.join(random.choice(chars) for x in range(size))


print(generate_new_paste_id())

