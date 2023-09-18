def quick_hoare(lo, hi):
    # 계속 갈지 말지 ...
    if lo >= hi: return

    # partition
    i, j = lo, hi
    p = arr[lo]             # pivot
    while i <= j:
        while i <= hi and p >= arr[i]:
            i += 1
        while p < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    # 분할 위치는 pivot이 있는 j
    quick_hoare(lo, j - 1)
    quick_hoare(j + 1, hi)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_hoare(0,N-1)
    print(f'#{tc} {arr[N//2]}')
