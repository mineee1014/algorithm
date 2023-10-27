# N : 에르다 노바 사용횟수
# M : 오리진 스킬 사용횟수
N, M = map(int, input().split())

erda = sorted(list(map(int, input().split())))
origin = sorted(list(map(int, input().split())))

# 에르다는 100초 쿨
# 오리진은 360초 쿨

# 쿨타임이 풀리는 시점을 계산할 변수
erda_cool = 0
origin_cool = 0

# 스킬은 사용한 횟수
erda_count = 0
origin_count = 0


# 에르다 스킬 버튼을 누른 시간을 하나씩 본다
for i in range(N):
    # 쿨타임이 풀리는 시점 "을 포함한 이후(이상)" 에르다 스킬 버튼을 눌렀다면 스킬을 사용할 수 있다
    if erda_cool <= erda[i]:
        # 스킬 쿨타임은 100초인데 면역 기간이 90초라면
        # 어차피 다시 스킬을 쓸 쿨타임이 올 때에는 이미 면역은 풀려있음

        # 스킬을 사용한 시점으로부터 쿨타임 100초를 더했을 때 시점에 쿨타임이 풀린다
        erda_cool = erda[i] + 100
        # 스킬을 사용한 횟수 -> 면역은 당연히 들어감
        erda_count += 1

for i in range(M):
    if origin_cool <= origin[i]:
        origin_cool = origin[i] + 360
        origin_count += 1
print(erda_count, origin_count)