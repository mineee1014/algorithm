num_lst = list(input())
length = len(num_lst)

for i in range(length):
    if num_lst[i] == '0':
        num_lst.pop(i)
        num_lst = list(map(int, num_lst))
        num_lst.sort(reverse=True)
        num_sum = 0
        for num in num_lst:
            num_sum += num
        if num_sum % 3 == 0:
            result = ''.join(list(map(str,num_lst)))
            print(result + '0')
        else:
            print(-1)

        break
else:
    print(-1)