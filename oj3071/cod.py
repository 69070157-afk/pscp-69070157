'''pap12345678'''

A = int(input())
B = int(input())
b = int(input())
r = int(input())

ae = (A-r)//b
be = (B-r)//b
P = be - ae
if A%b == r:
    P += 1

print(P)
