'''PPP'''

ca = float(input())
e1 = input().lower()
e2 = input().lower()

if e1 == 'k':
    c = ca - 273.15
elif e1 == 'f':
    c = ((ca - 32)*5)/9
elif e1 == 'r':
    c = ((ca*5)/9)-273.15
else:
    c = ca

if e1 == e2 :
    P = ca
elif e2 == 'k':
    P = c + 273.15
elif e2 == 'f':
    P = ((c*9)/5)+32
elif e2 == 'r':
    P = ((c+273.15)*9)/5
else:
    P = c

print(f'{P:.2f}')
