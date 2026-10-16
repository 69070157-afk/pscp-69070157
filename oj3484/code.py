'''eee'''
h , tx = map(int, input().split())
rery = []
for _ in range(h):
    rery.append(list(map(int,input().split())))
for i in rery:
    good = i.count(0)
    not_good = h - good
    print(*i,not_good,sum(i))
num = []
not_good_list = []
sum_x = []
for x in range(h):
    for y in range(h):
        num.append(rery[y][x])
    good = num.count(0)
    not_good = h - good
    not_good_list.append(not_good)
    sum_x.append(sum(num))
    num.clear()
print(*not_good_list)
print(*sum_x)
print(f'{sum(not_good_list)} {sum(sum_x)} {(sum(sum_x))*tx :.2f}')
