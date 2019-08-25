import re
import json

# f = open('abstracts_en.ttl','r', encoding='utf-8')
# l = f.readlines()
# lines = []
# buffer = []
# for i in l:
#     if i == '\n':
#         lines.append(buffer)
#         buffer = list()
#     else:
#         buffer.append(i[:-1])
# abstracts = {}
# mode = 0
# count = 0
# for line in lines:
#     context = None
#     for sentence in line:
#         if mode == 1:
#             subjectsearch = re.search(r'<http://dbpedia.org/resource/(.*)/abstract', line[0])
#             subject = subjectsearch.group(1)
#             abstracts[subject] = context
#             mode = 0
#         matches = re.search(r'nif:isString \"\"\"(.*)\"\"\"\^\^xsd:string;', sentence)
#         if matches:
#             context = matches.group(1)
#             mode = 1
#     if count == 10:
#         break

# with open('abstracts_data.json', 'w') as outfile:
#     json.dump(abstracts, outfile)
from pprint import pprint
with open('wikiData.json') as f:
    data = json.load(f)

# pprint(data['data'])
count = 0
for topic in data['data'][:10]:
    print(topic['paragraphs'][0]['context'])
    print(topic['paragraphs'][1]['context'])
    print(topic['paragraphs'][2]['context'])
    count += 1
    print(count)
    print('\n')
    if count  == 10:
        break
