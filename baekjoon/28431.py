lst = []
for _ in range(5):
    a = input()
    if a in lst:
        t = lst.index(a)
        lst.pop(t)
    else:
        lst.append(a)
print(lst[0])

