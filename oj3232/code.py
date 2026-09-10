'''PEPE1'''
x, y = input().split()
x = int(x)
y = int(y)
way = 0
i = 0
feet = 0
while way < y:
    i += 1
    feet = (x-(2*(i-1)))
    way += feet
    if feet <= 0 and way < y:
        i = -1
        break
print(i)
