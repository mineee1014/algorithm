N = int(input())
A = list(map(int, input().split()))
B = [0]
max_num = 0
def func(i,B):
    global max_num
    if i == N:
        if sum(B) > max_num:
            max_num = sum(B)



    for j in range(i, N):

        if B[-1] < A[j]:
            B.append(A[j])
            func(j+1, B)
            B.pop()
        else:
            continue

    else:
        if sum(B) > max_num:
            max_num = sum(B)


func(0,B)
print(max_num)