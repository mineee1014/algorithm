N = int(input())
word = [input() for _ in range(N)]
M = int(input())
cand = [input() for _ in range(M)]

if N != 1:
    a = word.index('?')
    if a == 0:
        for can in cand:
            if can[-1] == word[1][0] and can not in word:
                result = can
                break
    elif a == len(word)-1:
        for can in cand:
            if can[0] == word[-2][-1] and can not in word:
                result = can
                break
    else:
        for can in cand:
            if can[0] == word[a-1][-1] and can[-1] == word[a+1][0] and can not in word:
                result = can
                break
    print(result)
else:
    print(cand[0])