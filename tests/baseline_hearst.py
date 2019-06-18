'''
results can be found in baseline_results.txt

The following test has been run 1240 abstracts. 
The hearst patterns used can be found in syntaxnet_triplets/src/hpatterns
'''


import sys
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import HearstPatterns
from GSoC2019.conllu.conllu import parse_single, TokenList

conll_data_path = '../abstract_conll_data/'
onlyfiles = [f for f in listdir(conll_data_path) if isfile(join(conll_data_path, f))]

h = HearstPatterns()
count = 0 
results = open('test.txt', 'w')
for conll_file in onlyfiles[:]:
    count += 1
    try:
        hearst_patterns = h.find_hearstpatterns(conll_data_path + conll_file)
        results.write(conll_file + ' :- ' + str(hearst_patterns)+'\n')
    except:
        None
    
print(count)
results.close()



