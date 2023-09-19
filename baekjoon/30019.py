import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
room = [0] * (N+1)
for case in range(M):
    k, s, e = map(int, sys.stdin.readline().rstrip().split())
    if room[k] <= s:
        print('YES')
        room[k] = e
    else:
        print('NO')