import bibtexparser as bp
import codecs

with open('icml2011.bib') as bf:
    btstr = bf.read()

bib_database = bp.loads(btstr)

with codecs.open('icml2011.csv', 'w', encoding='utf-8') as fout:
    for x in bib_database.entries:
        fout.write('%s\t%s\n' % (x['author'], x['title']))
