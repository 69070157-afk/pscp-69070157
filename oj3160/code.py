'''PEP8'''
starte = input().split()
ende = int(starte[1])
starte = int(starte[0])
Total_primes = []
for i in range(starte,ende+1):
    n = 1
    if i < 2 or not i%2:
        n = 0
    else:
        for ie in range(3,(i//2)+1,2):
            if not i%ie:
                n = 0
                break
    if n == 1 or i == 2:
        Total_primes.append(i)
if Total_primes:
    print(*Total_primes)
print(f'Total primes: {len(Total_primes)}')
