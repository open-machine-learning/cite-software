import codecs
from bs4 import BeautifulSoup

html_fname = 'icml2007_allpapers/icml2007_proc.html'

all_authors = []
all_titles = []

with open(html_fname) as fout:
    soup = BeautifulSoup(fout.read(), 'html.parser')
    tds = soup.find_all("td")

    for td in tds:
        authors_start = '<td width="84%">'
        title_start = '<td colspan="2">'
        if str(td).startswith(authors_start):
            td = td.getText()
            authors = td.split(" - ")
            clean_authors = []
            for a in authors:
                if u"\r\n\t" in a:
                    clean_authors.append(a.split(u'\r\n\t')[-1])
                else:
                    clean_authors.append(a)
            authors = clean_authors
            authors = [a.strip() for a in authors]
            authors = [a for a in authors if len(a)]
            all_authors.append(u' and '.join(authors))
        elif str(td).startswith(title_start):
            td = td.getText()
            tokens = td.split('\n')
            if len(tokens) > 1:
                title = tokens[1].strip()
                all_titles.append(title)

with codecs.open('icml_metadata/icml2007.csv', 'w', encoding='utf-8') as fout:
    for title, authors in zip(all_titles, all_authors):
        fout.write('%s\t%s\n' % (title, authors))
