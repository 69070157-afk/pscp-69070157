'''EEE'''
n, si = map(int, input().split())
manu_dog_movie = {}
for i in range(1,n+1):
    manu_dog_movie[i] = int(input())
have = []
while True:
    if si not in have:
        have.append(si)
        si = manu_dog_movie.get(si,si)
        continue
    break
if 0 in have:
    print(len(have)-1)
else:
    print(len(have))
