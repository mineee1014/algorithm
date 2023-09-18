import sys
N = int(sys.stdin.readline().rstrip())
result = -(N-1)     # 마지막을 제외한 주어진 모든 멀티탭은 플러그를 하나씩 차지함
for case in range(N):
    # 멀티탭이 가진 용량만큼 추가
    result += int(sys.stdin.readline().rstrip())
print(result)