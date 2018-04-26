#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashley Anderson'
SITENAME = u':wq'
SITESUBTITLE = 'a catalog of stuff I happen to write down'
SITEURL = 'https://aga3.xyz'

THEME = './theme'
THEME_STATIC_DIR = './theme/static'
HEADER_COVER = '/images/piestewa_1024.jpg'

GITHUB_URL = 'http://github.com/aganders3'
TWITTER_URL = 'http://twitter.com/aganders3'

PATH = 'content'
STATIC_PATHS = ['images', 'images/projects', 'files', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

SLUGIFY_SOURCE = 'title'
COLOR_SCHEME_CSS = 'tomorrow_night.css' # 'monokai.css'
PYGMENTS_RST_OPTIONS = {'linenos' : 'table'}
DEFAULT_METADATA = {'Status' : 'draft'}

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%A %B %d, %Y'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
