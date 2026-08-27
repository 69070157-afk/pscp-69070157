'''PEP8'''
member = input()
n = int(input())
totty = 0
for _ in range(n):
    totty += float(input())
if member == 'Y':
    totty *= 0.95
else :
    if totty >= 500:
        totty *= 0.97
totty += 0.001
print(f'{totty:.2f}')
