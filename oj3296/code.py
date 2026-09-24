'''3296'''
rgb1 = input().split()
rgb2 = input().split()
rgb11 = int(rgb1[0])
rgb12 = int(rgb1[1])
rgb13 = int(rgb1[2])
rgb21 = int(rgb2[0])
rgb22 = int(rgb2[1])
rgb23 = int(rgb2[2])
rg1 = (rgb11+rgb21)//2
rg2 = (rgb12+rgb22)//2
rg3 = (rgb13+rgb23)//2
print(f'{rg1} {rg2} {rg3}')
