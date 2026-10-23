'''eee'''
txt = input()
non_cry = []
for i in txt[::-1]:
    if i not in non_cry:
        non_cry.append(i)
    else:
        non_cry.remove(i)
if not non_cry:
    print('fully paired')
else:
    for i in non_cry[::-1]:
        print(i,end='')
