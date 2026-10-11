'''PEPE'''
n = int(input())
m = int(input())
n_team = []
spy_ = []
for _ in range(n):
    n_team.append(int(input()))
for _ in range(m):
    m_team = int(input())
    if m_team in n_team:
        spy_.append(m_team)
spy_.sort(reverse=True)
if not spy_:
    print('Nope')
else:
    for i in spy_:
        print(i)
