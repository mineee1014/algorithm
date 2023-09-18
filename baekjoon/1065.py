N = int(input())

if N < 100:
    print(N)
else:
    if N == 1000:
        N = 999
    a = N // 100    # 2
    b = (N-a*100) // 10 # 1
    c = (N-a*100-b*10)  # 0
    if 0 <= b + (b-a) <=9 and b + (b-a) <= c:
        count = 1
    else:
        count = 0

    while a > 0:
        while b > 0:
            b -= 1
            if 0 <= b + (b-a) <= 9:
                count += 1
        a -= 1
        b = 10
    print(99 + count)