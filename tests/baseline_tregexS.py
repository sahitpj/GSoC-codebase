import sys
import json
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import TripleExtraction
from GSoC2019.syntaxnet_triplets.src.pipelines import Spotlight_Pipeline
from nltk.tokenize import sent_tokenize

abstract_data_path = '../abstracts_data.json'

with open(abstract_data_path) as json_file:
    abstracts_data = json.load(json_file)

textraction = TripleExtraction()
spipe = Spotlight_Pipeline()
# results = open('tregex_results2.txt', 'w')
count = 0
for key, value in abstracts_data.items():
    triplets = []
    # results.write(key + '\n')
    for sentence in sent_tokenize(value):
        triple = textraction.treebank(sentence)
        annotated_triple = ((spipe.annotate_word(triple[0][0]), triple[0][1]), triple[1], (spipe.annotate_word(triple[2][0]), triple[2][1]))
        triplets.append(annotated_triple)
        print(annotated_triple)
    # results.write(str(triplets)+'\n')
    print(triplets)
    count += 1
    if count == 5:
        break

# results.close()

