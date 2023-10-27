import sys
import math
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())

# 연결 정보를 저장할 딕셔너리
road_map = {}
for _ in range(M):
    dep, arr, cost = map(int, input().split())
    if dep in road_map:
        road_map[dep].append((arr, cost))
    else:
        road_map[dep] = [(arr, cost)]

A, B = map(int, input().split())

# 방문 여부를 저장할 딕셔너리
visited = {}

# 시작 정점에서 각 정점까지의 최단 거리를 저장할 딕셔너리
d = {}
d[A] = 0

# 시작 정점부터 탐색을 시작
heapQ = []
heappush(heapQ, (d[A], A))

while heapQ:
    weight, w = heappop(heapQ)

    # B에 도달하면 종료
    if w == B:
        break

    # 방문한 정점은 스킵
    if w in visited:
        continue

    visited[w] = True

    # 연결된 정점 탐색
    if w in road_map:
        for v, cost in road_map[w]:
            if v not in d or d[v] > d[w] + cost:
                d[v] = d[w] + cost
                heappush(heapQ, (d[v], v))

print(d[B])
