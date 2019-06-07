import json
import os

def cleaned(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

with open("output/abstracts_data.json") as json_file:
    abstracts_data = json.load(json_file)

count = 0
for key in list(abstracts_data.keys())[1250:]:
    command = 'echo "{}" | syntaxnet/parser.sh > output/abstract_conll_data/{}.conll'.format(cleaned(abstracts_data[key]), cleaned(key))
    os.system(command)
    if count == 3:
        break
