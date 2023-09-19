# idx : 공장의 인덱스
# cost : 현재 총 비용
def cal(idx, cost):
    global min_cost
    if idx == N:
        min_cost = cost
        return

    # 물건의 인덱스 i
    for i in range(N):
        # 물건을 이미 누가 생산했거나
        # 생산 비용을 더했을 때 이미 총 비용을 초과할 예정이면 생략 (백트래킹)
        if lst[i] == 1 or cost + cost_lst[i][idx] >= min_cost:
            continue

        cost += cost_lst[i][idx] # 물건 i에 대한 생산 비용 가산
        lst[i] = 1  # 물건 i 생산했음을 표시

        cal(idx+1, cost)

        # 초기화
        cost -= cost_lst[i][idx]
        lst[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cost_lst = [list(map(int, input().split())) for _ in range(N)]
    lst = [0] * N
    min_cost = 15*99
    cal(0, 0)
    print(f'#{tc} {min_cost}')