# publishconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your blog is hosted at the root of your custom domain:
SITEURL = 'https://www.leftengeist.xyz'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are usually configured for production feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True