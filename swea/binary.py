def binary_search(start, end, num, flag):

    mid = (start+end)//2

    if A[mid] == num:
        return True

    elif start == end:
        return False

    if num < A[mid]:
        if flag == False:
            return False
        else:
            return binary_search(start, mid-1, num, False)
    else:
        if flag == True:
            return False
        else:
            return binary_search(mid + 1, end, num, True)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in B:
        if binary_search(0,N-1,i,100) == True:
            count += 1
    print(f'#{tc} {count}')
