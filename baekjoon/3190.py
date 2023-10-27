N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

L = int(input())

info = [list(input().split()) for _ in range(L)]

time = 1


def rotation(C):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 오른쪽 회전하는 경우
    if C == 'D':
        return


    i,j = 0,0

    for X,C in info:
        X = int(X)
        # 회전을 해야 할 시간이 될 때 까지
        while time < X:

            i += di
            j += dj



