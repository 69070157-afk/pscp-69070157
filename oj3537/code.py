'''eee'''
crew = []
amous = []
while True:
    txt = input()
    if txt == 'Start':
        break
    name, status = txt.strip('{} ').split(':')
    name = name.strip(' "')
    status = status.strip(' "')
    crew.append(name)
    if status == 'Impostor':
        amous.append(name)
Alive = crew.copy()
Dead = []
amous_al = len(amous)
while True:
    txt = input()
    if txt == 'End':
        break
    Alive.remove(txt)
    Dead.append(txt)
    if txt in amous:
        amous_al -= 1
Alive.sort()
Dead.sort()
print(f'{amous_al} Impostor Remains')
print('***Alive***')
for i in Alive:
    if i in amous:
        print(f'{i} : Impostor')
    else:
        print(f'{i} : Crewmate')
print('***Dead***')
for i in Dead:
    if i in amous:
        print(f'{i} : Impostor')
    else:
        print(f'{i} : Crewmate')
