'''3299'''
import math
n ,num = map(int, input().split())
allnum = 0
starg = 0
while True:
    starg += 1
    allnum += starg
    if num <= allnum:
        break
n = math.ceil(starg/n)
print(f'{n}')
