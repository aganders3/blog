#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ashley Anderson'
SITENAME = ':wq'
SITESUBTITLE = 'a catalog of stuff I happen to write down'
SITEURL = '.'

PATH = 'content'
STATIC_PATHS = ['images', 'images/projects', 'extra/CNAME', 'notebooks']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

SLUGIFY_SOURCE = 'title'
COLOR_SCHEME_CSS = 'tomorrow_night.css' # 'monokai.css'
PYGMENTS_RST_OPTIONS = {'linenos' : 'table'}
DEFAULT_METADATA = {'Status' : 'draft'}

# USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%A %B %d, %Y'

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['/Users/ash/src/Not Work/pelican-plugins']
PLUGINS = ['render_math']

MATH_JAX = {'align' : 'left', 'indent' : '3cm'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './theme'
THEME_STATIC_DIR = './theme/static'
HEADER_COVER = '/images/piestewa_1024.jpg'
