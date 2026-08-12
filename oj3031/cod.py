'''PAPE2'''
import math
n = input().split()
S = int(n[0])
PI = 3.1416
EI = [0]*(int(n[1]))
for i in range(int(n[1])):
    lo = input().split()
    x = int(lo[0])
    y = int(lo[1])
    rang = (x**2)+(y**2)
    ar = PI*rang
    chark = math.ceil(ar / S)
    EI[i] = int(chark)
for i in EI :
    print(i)
