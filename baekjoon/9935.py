word = input()
boom = input()
word_len = len(word)
boom_len = len(boom)
i = 0
stack_word = []
stack_check = []

while i < word_len:

    if len(stack_word) < boom_len-1:   # stack에 확인할 단어개수보다 적으면 그냥 append
        stack_word.append(word[i])
    else:
        if word[i] == boom[boom_len-1]:
            stack_check.append(word[i])
            for j in range(boom_len-2,-1,-1):
                # stack_word에서 글자 하나를 빼서 확인
                check = stack_word.pop()
                stack_check.append(check)
                if check == boom[j]:
                    continue
                else:
                    while stack_check:
                        stack_word.append(stack_check.pop())
                    break
            else:
                stack_check = []


        else:
            stack_word.append(word[i])
    i += 1

if not stack_word:
    print('FRULA')
else:
    print(''.join(stack_word))
