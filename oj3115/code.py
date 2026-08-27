'''pep888'''
num ,check = input().split()
num = int(num)
check = int(check)
start = [0]*num
stop = [0]*num
for i in range(num):
    start[i] ,stop[i] = input().split()
    start[i] = int(start[i])
    stop[i] = int(stop[i])
checktime = input().split()
opens = 0
for i in range(check):
    for ie in range(num):
        if start[ie] <= int(checktime[i]) < stop[ie]:
            opens += 1
    print(opens ,end=' ')
    opens = 0
