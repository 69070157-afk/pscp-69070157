'''3360'''

w, h, _, _ = map(int, input().split())
x_ilst = list(map(int, input().split()))
y_ilst = list(map(int, input().split()))
x_sinz = []
brean_sinz = []
num_x = 0
num_y = 0
y_sinz = []
x_ilst.append(w)
y_ilst.append(h)
x_ilst.sort()
y_ilst.sort()
for i in x_ilst:
    x_sinz.append(i-num_x)
    num_x = i
for i in y_ilst:
    y_sinz.append(i-num_y)
    num_y = i
x_sinz.sort()
y_sinz.sort()
for x in x_sinz:
    for y in y_sinz:
        brean_sinz.append(y*x)
#print(x_sinz)
#print(y_sinz)
#print(brean_sinz)
print(max(brean_sinz),end=' ')
brean_sinz.remove(max(brean_sinz))
print(max(brean_sinz))
