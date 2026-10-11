'''eee'''
num_lite = []
while True:
    num = int(input())
    if num != -1:
        num_lite.append(num)
    else:
        break
def get_ilst(ilst_i,index_i):
    '''eee'''
    if len(ilst_i) > index_i >= 0:
        return ilst_i[index_i]
    return -1
txt = []
runing = False
for i,_ in enumerate(num_lite):
    if get_ilst(num_lite,i) == get_ilst(num_lite,i+1)-1 :
        if not runing:
            runing = True
            txt.append(num_lite[i])
            txt.append('-')
    else:
        txt.append(num_lite[i])
        runing = False
#print(*txt)
bare = False
frint = False
c = False
for i,_ in enumerate(txt):
    if txt[i] == '-':
        bare = True
    if not frint:
        print(txt[i],end='')
        frint = True
        continue
    if bare:
        print(f'-{txt[i+1]}',end='')
        bare = False
        c = True
        continue
    if c:
        c = False
        continue
    print(f', {txt[i]}',end='')
