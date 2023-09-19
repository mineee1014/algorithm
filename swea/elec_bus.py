def calc(idx, cnt):
    global min_cnt
    # 이미 최소 카운트를 넘긴 경우
    if cnt >= min_cnt:
        return
    # 도착 지점에 도착 (제약조건에 걸리지 않고)
    elif idx == N - 1:
        min_cnt = cnt
        return

    # 이번 정류장이 갈 수 있는 모든 거리
    for i in range(1, M[idx] + 1):
        # 정류장 도착 이후는 필요 없음
        if idx + i > N - 1:
            return
        calc(idx + i, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N, M = arr[0], arr[1:]
    min_cnt = N
    calc(0, -1)
    print(f'#{tc} {min_cnt}')