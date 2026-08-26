'''pEP*'''
way = input()
wat = float(input())
p = 0
if way == 'BKK CNX':
    p = 10+(wat*30)
elif way == 'CNX UBP':
    p = 15+(wat*40)
elif way == 'UBP BKK':
    p = 20+(wat*40)
elif way == 'BKK PKT':
    p = 25+(wat*50)
elif way == 'PKT CNX':
    p = 30+(wat*60)
elif way == 'UBP PKT':
    p = 40+(wat*70)
else:
    p = 'Error'
if p == 'Error':
    print(p)
else:
    print(f'{p:.2f}')
