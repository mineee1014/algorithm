def work(idx, percent):
    global max_work
    if idx == N:
        max_work = percent
        return

    for i in range(N):
        if lst[i] == 1 or P[idx][i] == 0 or percent * P[idx][i] / 100 < max_work:
            continue
        percent *= P[idx][i] / 100
        lst[i] = 1
        work(idx+1, percent)
        percent /= P[idx][i] / 100
        lst[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    max_work = 0
    lst = [0] * N
    work(0,1)
    print('#{} {:.6f}'.format(tc, max_work*100))

