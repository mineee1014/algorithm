import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
adj_m = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    adj_m[A].append((B, C))
    adj_m[B].append((A, C))


heapQ = []
heappush(heapQ, (0,1))
d = [1000000] * (V+1)
visited = [0] * (V+1)
result = 0


while heapQ:
    wei, w = heappop(heapQ)

    if visited[w] == 1:
        continue

    result += wei


    for v, weight in adj_m[w]:
        heappush(heapQ, (weight, v))

    visited[w] = 1

print(result)
