X = input()

info = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}

result = 0
t = 0

if X[0] == '0':

    if X[1] == 'x':
        bad = 16
        sad = 1
    else:
        bad = 8
        sad = 0

    for i in range(len(X) - 1, sad, -1):

        if X[i] in info:
            good = info[X[i]]
        else:
            good = int(X[i])

        result += good * bad ** t
        t += 1
    print(result)

else: print(X)
