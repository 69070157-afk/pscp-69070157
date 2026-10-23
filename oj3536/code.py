'''eee'''
def main():
    '''eee'''
    n = int(input())
    if n < 2:
        print('NO')
    else:
        i = 2
        while i * i <= n:
            if not n % i:
                print('NO')
                break
            i += 1
        else:
            print('YES')
main()
