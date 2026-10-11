'''PEPE8'''
for _ in range(int(input())):
    xy_ilse = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        xy = x + y
        xy_ilse.append([xy,y,x])
    xy_ilse.sort(key=lambda xy: (xy[0],-xy[1]))
    for i in xy_ilse:
        print(i[2],i[1])
