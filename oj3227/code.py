'''PEP*'''
cade = input().upper()
if len(cade) == 3:
    f = cade[:2]
    b = cade[2:]
else:
    f = cade[0]
    b = cade[1]
name_f = ''
name_b = ''
if f == 'Q':
    name_f = 'queen'
elif f == 'K':
    name_f = 'king'
elif f == 'J':
    name_f = 'jack'
elif f == 'A':
    name_f = 'ace'
else:
    name_f = f
if b == 'D':
    name_b = 'diamonds'
elif b == 'H':
    name_b = 'hearts'
elif b == 'S':
    name_b = 'spades'
else:
    name_b = 'clubs'
print(f'{name_f} of {name_b}')
