from collections import deque

def bfs(now, cnt):
    global min_cnt
    cnt += 1
    q = deque()
    q.append(now)
    visited[now] = 1

    while q:
        v = q.popleft()
        w = visited[v]
        lst = [v + 1, v - 1, v * 2, v - 10]
        for to in lst:
            if to <= 0 or to > 1000000:
                continue
            if visited[to] != 0:
                continue
            if to == M:
                if min_cnt > w:
                    min_cnt = w
                return

            visited[to] = w + 1
            q.append(to)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    min_cnt = 1000000

    bfs(N, 0)
    print(f'#{tc} {min_cnt}')