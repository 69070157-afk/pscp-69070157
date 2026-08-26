'''PPP'''
n = int(input())
hi = 0
low = 0
rang = 1
al = 0
H = 0
i = 0
while 1 :
    al += rang
    low = al-(rang-1)
    hi = al
    i += 1
    rang += 2
    if low <= n <= hi :
        H = i
        break


if not H%2 :
    if not n%2 :
        P = (H-1)*2
    else :
        P = ((H-1)*2)-1
else :
    if not n%2 :
        P = ((H-1)*2)-1
    else :
        P = (H-1)*2

print(P)
