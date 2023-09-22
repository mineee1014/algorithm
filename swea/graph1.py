def find_set(x):
    if parent[x] == x:
        return x

    return find_set(parent[x])

def union(x,y):

    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y :
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for i in range(M):
        union(arr[2*i],arr[2*i+1])

    print(f'#{tc} {len(set(parent[1:]))}')