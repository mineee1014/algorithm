A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
A = A1*B2 + B1*A2
A_new = A1*B2 + B1*A2
B = B1 * B2
lst = []
i = 2
t = max(B1, B2)
while i <= t:
    while B1 % i == 0:
        lst.append(i)
        B1 //= i
    while B2 % i == 0:
        lst.append(i)
        B2 //= i
    i += 1

for j in lst:
    if A % j == 0:
        A //= j
print(A, B//(A_new//A))