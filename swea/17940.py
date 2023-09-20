from itertools import combinations
def case(num):
    if num == 0:
        print(record)


    for i in range(B-A+1):

        if num - arr[i] < 0:
            return
        record[arr[i]] += 1
        case(num - arr[i])
        record[arr[i]] -= 1





T = int(input())
for tc in range(1,T+1):
    N, A, B = map(int, input().split())
    arr = [i for i in range(A,B+1)]
    record = [0] * (B+1)
    case(N)