import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
S = [sys.stdin.readline().rstrip() for _ in range(N)]
lst = {}
for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word not in lst:
        lst[word] = 1
    else: lst[word] += 1
cnt = 0
for key in lst:
    if key in S:
        cnt += lst[key]
print(cnt)