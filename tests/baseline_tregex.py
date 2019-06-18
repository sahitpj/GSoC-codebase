import sys
import json
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import TripleExtraction
from nltk.tokenize import sent_tokenize

abstract_data_path = '../abstracts_data.json'

with open(abstract_data_path) as json_file:
    abstracts_data = json.load(json_file)

textraction = TripleExtraction()
results = open('tregex_results2.txt', 'w')
count = 0
for key, value in abstracts_data.items():
    triplets = []
    results.write(key + '\n')
    for sentence in sent_tokenize(value):
        triple = textraction.treebank(sentence)
        triplets.append(triple)
    results.write(str(triplets)+'\n')
    count += 0
    if count == 5:
        break

results.close()

