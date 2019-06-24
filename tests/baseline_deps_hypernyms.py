import sys
import json
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import TripleExtraction_Deps
from nltk.tokenize import sent_tokenize

abstract_data_path = '../abstracts_data.json'

with open(abstract_data_path) as json_file:
    abstracts_data = json.load(json_file)

textraction = TripleExtraction_Deps()
# results = open('deps_hypernyms_results2.txt', 'w')
count = 0
for key, value in list(abstracts_data.items())[350:]:
    triplets = []
    # results.write(key + '\n')
    for sentence in sent_tokenize(value):
        dependencies = textraction.dependency_triplets(sentence)
        hypernyms = textraction.short_relations(dependencies, 2)[2]
        triplets.append(hypernyms)
    # results.write(str(triplets)+'\n')
    count += 0
    print(triplets)
    if count == 5:
        break

# results.close()
