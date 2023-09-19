arr = [i for i in range(1,11)]
sub = []
def subset(lst):
    if sum(lst) == 10: print(lst)

    for num in arr:


       if num not in lst:
           lst.append(num)

           if sum(lst) > 10:
               pass
           else: subset(lst)

           lst.pop()

subset(sub)