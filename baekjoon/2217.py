
N = int(input())
rope = sorted([int(input()) for _ in range(N)], reverse=True)
rope_num = len(rope)
i = 0
max_weight = 0
while i < N:
    if max_weight < rope[i] * (i+1):
        max_weight = rope[i] * (i+1)
    i += 1

print(max_weight)
