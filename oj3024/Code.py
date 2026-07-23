'''PAP8'''

al = float(input())
hi = float(input())                                                                                                                                                                                                  
e1 = al - hi
for i in range(int(hi),-1,-1) :
    if e1 - float(i) >= 0 :
        mid = float(i)
        break
low = al - (hi + mid)
if hi - low > 2 :
    E = 'Surprising'
else :
    E = 'Not surprising'
print(E)
