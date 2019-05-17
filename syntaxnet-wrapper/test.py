import pyconll

FILEPATH = 'output/sample.conll'

f = open(FILEPATH)
l = f.readlines()
table = []
for i in l:
    k = i.split('\t')
    k = k[:-1]
    table.append(k)
print(table)