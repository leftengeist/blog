import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = 'Admin'
SITENAME = 'My Test Blog'
SITEURL = 'https://www.leftengeist.xyz'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll / Links
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
)

DEFAULT_PAGINATION = 5
