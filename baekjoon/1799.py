import random
import copy

def generate_random_chessboard(size):
    chessboard = []
    for _ in range(size):
        row = [random.randint(0, 1) for _ in range(size)]
        chessboard.append(row)
    return chessboard

def print_chessboard(chessboard):
    for row in chessboard:
        print(" ".join(map(str, row)))




def check(case_num):
    global bishop
    # 델타
    di = [i for i in range(1,N)]
    dj = [i for i in range(1,N)]

    # 체스판의 모든 칸에 대해 순회
    for i in range(N):
        for j in range(N):

            # 놓을 수 없는 칸이면 넘어가기
            if boards[i][j] == 0:
                continue

            lst = [(i, j)]
            cnt = 0

            # 델타의 인덱스
            for t in range(N - 1):
                # 선택한 지점을 기준으로 총 네 방향의 대각선에 대해 순회
                for a, b in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    idx_i = i + a * di[t]
                    idx_j = j + b * dj[t]
                    # 올바른 인덱스 안에 있는 값만 필터링
                    if 0 <= idx_i < N and 0 <= idx_j < N:

                        # 영향을 줄 수 있는 빈 칸이 있는지 확인
                        if boards[idx_i][idx_j] == 1:
                            cnt += 1
                            lst.append((idx_i, idx_j))

                # 백트래킹 조건 1
                # 영향을 줄 수 있는 칸이 많으면 다음에 보자
            if cnt > case_num:
                continue

            # 영향을 받는 빈 칸이 최소라면 비숍 카운트 후 나머지 칸 색칠
            # 백트래킹 조건 1의 break 에 걸리지 않았을 때만 실행
            if cnt <= case_num:
                bishop += 1
                while lst:
                    a, b = lst.pop()
                    boards[a][b] = 0
    else:
        return False




def dfs(n, cnt):
    global ans
    # 남은 대각선을 다 놓아도 갱신 X(가지치기)
    if cnt+(K+1-n)//2<=ans:
        return
    if n>=K:    # 모든 대각선에 비숍을 놓아보면 종료 (종료조건)
        ans = max(ans, cnt)
        return
    for (ci,cj) in lst[n]:
        if v[ci-cj]==0:     # 미방문할 경우
            v[ci-cj]=1
            dfs(n+2, cnt+1) # 해당 위치에 비숍 놓고 다음 대각선(+2인 경우는 마지막 주석 참고)
            v[ci-cj]=0
    # 이 대각선에 안놓고 다음으로 가는 것 -> 더 많을 수 있음
    dfs(n+2, cnt)           # 안 놓고 가는 경우

for tc in range(500):
    N = random.randint(1,4)
    # 체스판의 정보
    boards = generate_random_chessboard(N)
    new = copy.deepcopy(boards)
    arr = boards

    # 값 입력받고 비숍 위치 리스트 생성
    K = N*2-1
    lst = [[] for _ in range(K)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:    # 비숍 가능 위치
                lst[i+j].append((i,j))

    v = [0]*(2*N)               # 대각선 중복체크

    # 여기서 크게 확인할 포인트는 체스 특성 상 비숍은 흑색칸만 다니거나 백색칸만 다닐 수 있기 때문
    # 매 대각선을 확인하는 것이 아니라 2씩 넘어가면서 확인해도 됨 -> 시간 단축 가능
    ans = 0
    dfs(0, 0)
    t, ans = ans, 0
    dfs(1, 0)


    bishop = 0
    i = 0
    while i <= 2 * N:
        if check(i):
            i = 0
        else:
            i += 1

    if ans+t != bishop:
        print(N)

        print(f'case1 : {ans+t}')
        print(f'case2 : {bishop}')

        for _ in range(N):
            print(*new[_])