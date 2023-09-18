def func(n,dd):
    if n == 1 or n == 0 or n == 2:
        return 'YES'
    f = 1
    i = 1
    while f*(i+1) <= n:
        i += 1
        f *= i
    if i == dd:
        return 'NO'
    else:
        return func(n-f,i)

N = int(input())
if N == 0:
    print('NO')
else:
    print(func(N,100000))