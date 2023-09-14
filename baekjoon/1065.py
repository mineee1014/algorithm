N = int(input())

if N < 100:
    print(N)
else:
    a = N // 100
    b = (N-a) // 10
    c = (N-a-b)

    while True: