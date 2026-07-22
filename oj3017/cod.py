'''PAP8'''
totla_raw = int(input())
swt = totla_raw*0.1
tex = totla_raw*0.07
SW = float()

if (swt) <= 50 :
    SW = 50
elif (swt) >= 1000 :
    SW = 1000
else :
    SW = swt
tex = (totla_raw + SW)*0.07
totla = tex + SW + totla_raw
print(f'{totla :.2f}')
