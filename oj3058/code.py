'''ppp'''
a = int(input())
b = int(input())
goal = int(input())

B = min(goal//5,b)
A = goal-(B*5)
if a >= A :
    P = A
else :
    P = -1
print(P)
