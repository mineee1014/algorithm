from heapq import heappop, heappush
T = int(input())
for tc in range(1, T+1):


    N = int(input())
    # 지도
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 실제로 소모한 연료가 저장될 행렬, 무수히 큰 값으로 초기화
    F = [[10000000000000]*N for _ in range(N)]
    # 시작 위치는 연료 0으로 설정
    F[0][0] = 0

    # 인접하여 있는지 확인할 델타
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    Q = []
    heappush(Q, (F[0][0], (0,0)))

    while Q:
        # 확인해 볼 정점
        fuel, w = heappop(Q)
        i, j = w
        for t in range(4):
            idx_i = i+di[t]
            idx_j = j+dj[t]
            # 유효한 인덱스에 있는 인접 정점을 필터
            if 0<=idx_i<N and 0<=idx_j<N:
                # 기본적으로 1 소모
                fuel_consume = 1
                # 현재 정점과 인접 정점과의 높이 비교를 통해 소모 연료 계산
                if arr[i][j] < arr[idx_i][idx_j]:
                    fuel_consume += arr[idx_i][idx_j] - arr[i][j]

                # 인접 정점까지 이동하는데 소모되는 연료가 작다면
                if fuel + fuel_consume < F[idx_i][idx_j]:
                    # 기록
                    F[idx_i][idx_j] = fuel + fuel_consume
                    heappush(Q, (F[idx_i][idx_j], (idx_i, idx_j)))

    print(f'#{tc} {F[N-1][N-1]}')