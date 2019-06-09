import json
import os

def cleaned(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

with open("output/abstracts_data.json") as json_file:
    abstracts_data = json.load(json_file)

count = 0
for key in ["Haggai"]:  #list(abstracts_data.keys())[1250:]
    command = 'echo "{}" | syntaxnet/parser.sh > output/trial/{}.conll'.format(cleaned(abstracts_data[key]), cleaned(key))
    os.system(command)
    if count == 3:
        break


'''
Test - 1

1. Asexual_reproduction (thing)
2. Simonides_of_Ceos (place)
3. Hawaii


Test - 2

1. Anger (thing)
2. Osman_I (person)
3. Lillehammer (place)

Test - 3

1. Amalthea_%28moon%29 (thing)
2. David_Zindell (person)
3. Himachal_Pradesh (place)
'''