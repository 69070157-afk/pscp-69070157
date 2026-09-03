'''PEP8'''
n, k, t = map(int, input().split())
present = True
number = 1
i = 0
while present :
    if number == t:
        present = False
    number += k
    while number > n:
        number -= n
    i += 1
    if number == 1:
        break
print(i)
