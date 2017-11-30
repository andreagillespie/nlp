vocab = ['n-grams associated with research category (can be found with bigram/trigram collocations)']

import re
def find_ngram(abstract):
    count = 0
    for i in vocab:
        if i in abstract.lower():
            count += 1
    
    if count > 0:
        pmid = re.search(r'PMID: \d{8}', abstract, flags=0)
        pmid = re.sub(r'\D', "", str(pmid.group())) + '\n'
	      print pmid
	      match.write(str(pmid))
    if count < 1:
	      pmid = re.search(r'PMID: \d{8}', abstract, flags=0)
	      if 'sre' in str(pmid):
            pmid = re.sub(r'\D', "", str(pmid.group())) + '\n'
        mismatch.write(str(pmid))

hits = open('filename of XML output of search-script')
hits = str(hits.read())
match = open('matchfilename', 'r+')
mismatch = open('mismatchfilename', 'r+')

hitid = re.findall(r'\d{8}</PMID>', hits, flags=0)
    
for i in hitid:
    abid = re.sub(r'\D', "", i)
    ab = 'filename containing each absract to be tested named by PMID/' + abid
    abst = open(ab)
    abstract = str(abst.read())
    print find_ngram(abstract)
