# 지도의 최대 크기는 8*8이므로 계산복잡도 크지 않음
# 브루트포스 해도 될 크기인듯함

# 벽 세우는 규칙
# 0에다 세워야 하므로 BFS로 구현해볼까?
import sys
sys.stdin.readline().rstrip()
from collections import deque
from itertools import combinations
from copy import deepcopy

# 바이러스 다 퍼진 값 찾는 함수
def bfs_virus(virus, arr):
    # 상하좌우 델타함수 작성
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    for x, y in virus:
        Q = deque()
        Q.append((x, y))

        while Q:
            i, j = Q.popleft()

            for k in range(4):
                idx_i = i + di[k]
                idx_j = j + dj[k]
                # 유효한 좌표인지 검사
                if 0 <= idx_i < N and 0 <= idx_j < M:
                    # 빈 통로일 때만 퍼질 수 있으므로 0 일 때
                    if arr[idx_i][idx_j] == 0:
                        # 바이러스 퍼짐
                        arr[idx_i][idx_j] = 2
                        # 큐에다 추가
                        Q.append((idx_i, idx_j))
    return arr


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 초기 바이러스의 위치를 담아둘 리스트
virus = []
# 빈 칸의 위치를 담아둘 리스트
wall = []
#
max_safe_area = 0

# 지도 순회
for i in range(N):
    for j in range(M):
        if lst[i][j] == 2:
            virus.append((i,j))
        elif lst[i][j] == 0:
            wall.append((i,j))

for wall_case in combinations(wall,3):
    # 벽 세워버리기
    for i, j in wall_case:
        lst[i][j] = 1
    result = bfs_virus(virus,deepcopy(lst))
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if result[i][j] == 0:
                safe_area += 1

    if safe_area > max_safe_area:
        max_safe_area = safe_area

    # 벽 무너뜨리기
    for i, j in wall_case:
        lst[i][j] = 0

print(max_safe_area)