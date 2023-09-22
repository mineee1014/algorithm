M, N = map(int, input().split())
if M == 1:
    M += 1
arr = [1] * (N+1)
i = 2
while i < M:
    if arr[i] == 0:
        i += 1
        continue
    j = 1
    while i*j <= N:
        arr[i*j] = 0
        j += 1
    i += 1
for t in range(M,N+1):
    if arr[t] == 0:
        continue
    print(t)
    j = 1
    while t*j <= N:
        arr[t*j] = 0
        j += 1