arr = [input() for _ in range(3)]

lst = ['Fizz', 'Buzz', 'FizzBuzz']

for word in arr:
    if word not in lst:
        x = arr.index(word)
        num = word
        break
result = int(num) + 3-x

if result % 15 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)