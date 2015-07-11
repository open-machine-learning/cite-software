#!/usr/bin/env python

import glob

import bs4
import codecs


###############################################################################

def scrape_html(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as page:
        tree = bs4.BeautifulSoup(page.read())
        title = tree.findAll(name='meta', attrs=dict(name='citation_title'))[0]
        title = title.attrs['content']
        authors = tree.findAll(name='meta', attrs=dict(name='citation_author'))
        authors = [a.attrs['content'] for a in authors]
    return title, authors




with codecs.open('../icml_metadata/icml2013.csv', 'w',
                 encoding='utf-8') as outfile:
    for filename in glob.glob('../icml2013/*.html'):
        if filename.endswith('index.html'):
            continue
        title, authors = scrape_html(filename)
        outfile.write('%s\t%s\n' % (' and '.join(authors), title))



