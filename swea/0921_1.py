from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):

    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(E):
        u, v, weight = map(int, input().split())
        # 유향
        G[u].append((v, weight))

    # 초기값 설정 중요!!!!!!!
    # D[v] => 출발점에 v 정점까지 최단 거리
    D = [0xfffff] * (N + 1)
    D[0] = 0
    Q = []
    # 큐에 삽입 할 때 (D[v], v)
    heappush(Q, (0, 0))

    while Q:
        dist, u = heappop(Q)
        # 정점 u는 최단경로가 확정된다.
        if dist > D[u]: continue

        for v, weight in G[u]:
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                heappush(Q, (D[v], v))

    print(f'#{tc} {D[N]}')