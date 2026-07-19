'''PAP8'''
mon = int(input())
day = int(input())
W = 'winter'
SP = 'spring'
SM = 'summer'
F = 'fall'
if not mon%3 :
    if day >= 21 :
        if 1 <= mon <=3 :
            SS = SP
        elif 4 <= mon <=6 :
            SS = SM
        elif 7 <= mon <= 9 :
            SS = F
        else :
            SS = W
    else :
        if 1 <= mon <=3 :
            SS = W
        elif 4 <= mon <=6 :
            SS = SP
        elif 7 <= mon <= 9 :
            SS = SM
        else :
            SS = F
else :
    if 1 <= mon <=3 :
        SS = W
    elif 4 <= mon <=6 :
        SS = SP
    elif 7 <= mon <= 9 :
        SS = SM
    else :
        SS = F
print(SS)
