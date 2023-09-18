N, L = map(int, input().split())
arr = list(map(int, input().split()))
pipe = [0] * (1001+L)
for fix in arr:
    pipe[fix] = 1

count = 0
for i in range(1001):
    if pipe[i] == 1:
        for j in range(L):
            pipe[i+j] = 0
        count += 1
print(count)