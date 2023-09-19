A, B = map(int, input().split())
# 패티가 치즈보다 많다면
if A > B:
    print(B+B+1)
# 치즈가 패티보다 더 많거나 같다면
else:
    print(A+A-1)