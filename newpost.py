#!/usr/bin/env python
from __future__ import division, print_function

import argparse
import datetime
import os
import sys
import textwrap
from subprocess import call

def slugify(string):
    import re
    slug = re.sub(r'[^\w]+', '-', string)
    slug = slug.lower()
    return slug

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Pelican article template")
    parser.add_argument('title', nargs='+')
    parser.add_argument('-md', action='store_const', const=True, default=False)
    parser.add_argument('--category', nargs="?", default='')
    parser.add_argument('--tags', nargs="+", default='')
    args = parser.parse_args()

    num_articles = len(os.listdir('./content/articles'))

    title = ' '.join(args.title)
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    slug = slugify(title)

    if args.md:
        header_string = """\
        Title: {title}
        Date: {date_string}
        Category: {category}
        Tags: {tags}
        Slug: {slug}
        Author: Ashley Anderson
        Summary:
        Header_Cover: /images/piestewa_1024.jpg
        """
    else:
        header_string = """\
        {title}
        {title_bar}
        :date: {date_string}
        :category: {category}
        :tags: {tags}
        :slug: {slug}
        :author: Ashley Anderson
        :summary:
        :header_cover: /images/piestewa_1024.jpg
        """

    header_string = textwrap.dedent(header_string)
    header = header_string.format(title=title,
                                  title_bar='#'*len(title),
                                  date_string=date_string,
                                  category=args.category,
                                  tags=', '.join(args.tags),
                                  slug=slug)

    fname = './content/articles/{:04d}-{}'.format(num_articles, slug)
    fname = fname + ('.rst' if not args.md else '.md')
    with open(fname, 'w') as new_article:
        new_article.write(header)
    call(['vim', fname])
