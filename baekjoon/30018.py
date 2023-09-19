N = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
result = 0
for i in range(N):
    if arr_a[i] - arr_b[i] > 0:
        result += arr_a[i] - arr_b[i]
print(result)