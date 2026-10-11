'''3357'''
line = []
n = int(input())
full = 0
for _ in range(n):
    line.append(int(input()))
def git_list(listi,idnex_i):
    '''3357'''
    if len(listi) > idnex_i >= 0:
        return listi[idnex_i]
    return 0
for i in range(n):
    if git_list(line,i) > git_list(line,i+1) and git_list(line,i) > git_list(line,i-1):
        full += 1
        #print(f'full {git_list(line,i)}')
    #else:
        #print(f'{git_list(line,i)}not_full')
    #print(git_list(line,i) > git_list(line,i+1),git_list(line,i) > git_list(line,i-1))
print(full)
