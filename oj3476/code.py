'''eee'''
from collections import Counter
n = int(input())
name = {}
for _ in range(n):
    txt = input().replace('"', '').replace('{', '').replace('}', '').strip()
    namee, tp = txt.split(':')
    namee = namee.strip()
    tp = tp.strip()
    name[namee] = [tp[:3], tp[3:].strip()]
def has(kind, num):
    '''eee'''
    return any(v[0] == kind and int(v[1]) == num for v in name.values())
if 'Garfield' not in name and not has('Cat', 1):
    name['Garfield'] = ['Cat', '01']
if 'Fubuki' not in name and not has('Fox', 1):
    name['Fubuki'] = ['Fox', '01']
cont = Counter(v[0] for v in name.values())
print(f'Cat : {cont["Cat"]}')
print(f'Fox : {cont["Fox"]}')
for k, v in sorted(name.items(), key=lambda i: (i[1][0] != 'Cat', int(i[1][1]))):
    print(f'{k} : {v[0]}{v[1]}')
