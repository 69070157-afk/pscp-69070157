''' PAP8'''

c1 = input()
c2 = input()
SE = ['Red','Blue','Yellow']
CON1 = int()
CON2 = int()
C3 = str()

if c1 in SE and c2 in SE:

    if  c1 == c2  :
        C3 = c1
    else :
        if c1 == 'Red':
            CON1 = 1
        elif c1 == 'Blue':
            CON1 = 2
        else :
            CON1 = 3
        if c2 == 'Red':
            CON2 = 1
        elif c2 == 'Blue':
            CON2 = 2
        else :
            CON2 = 3
        if CON1 + CON2 == 3 :
            C3 = 'Violet'
        elif CON1 + CON2 == 4:
            C3 = 'Orange'
        elif CON1 + CON2 == 5:
            C3 = 'Green'
        else :
            C3 = 'Error'
else:
    C3 = 'Error'

print(C3)
