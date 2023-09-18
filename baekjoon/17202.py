def func(arr):
    len_arr = len(arr)
    if len_arr == 2:
        result = str(arr[0])+str(arr[1])
        return result
    new_arr = []
    for i in range(len_arr-1):
        new_arr.append((arr[i]+arr[i+1])%10)
    return func(new_arr)


A = input()
B = input()
arr = []
for i in range(8):
    arr.append(int(A[i]))
    arr.append(int(B[i]))
print(func(arr))