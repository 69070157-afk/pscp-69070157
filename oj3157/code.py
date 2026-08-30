'''PEP8'''
score = 0
for _ in range(int(input())):
    if input() == '+':
        score += 10
    else:
        score -= 5
print(score)
