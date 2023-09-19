A, B = map(int, input().split())
if B < A <= 2*B:
    print('YES')
    K = A-B
    print(K)
    for _ in range(K-1):
        print('aba')
    S = 'a'
    for i in range(B-K+1):
        S += 'ba'
    print(S)
else: print('NO')