def combination():
    global min_paper
    # idx 는 튜플
    idx = find_1()
    if not idx:
        if sum(papers) < min_paper:
            min_paper = sum(papers)
        return

    x, y = idx

    # 어느 한 종이라도 5개 이상 초과했다면
    for size in papers:
        if size > 5:
            return

    # 색종이의 크기 종류
    size_lst = [1,2,3,4,5]
    # 한번씩 색종이 대보기
    for size in size_lst:
        # 인덱스를 초과하여 들어갈 수 없는 색종이면 통과
        if x + size - 1 >= 9 or y + size - 1 >= 9 or find_0(x,y,size):
            break

        # 통과했으면 한번씩 칠해보자
        for i in range(x, x+size):
            for j in range(y, y+size):
                arr[i][j] = 0

        # 내가 사용한 색종이 카운트
        papers[size] += 1

        combination()

        # 다시 칠해보자
        for i in range(x, x+size):
            for j in range(y, y+size):
                arr[i][j] = 1

        papers[size] -= 1

def find_1():
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                return (i, j)
    return False

def find_0(x,y,size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] == 0:
                return True
    return False


arr = [list(map(int, input().split())) for _ in range(10)]
min_paper = 1000000000000000
papers = [0]*6
combination()
if min_paper == 1000000000000000:
    print(-1)
else: print(min_paper)