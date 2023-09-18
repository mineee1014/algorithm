board = input() + '.'
len_board = len(board)
i = 0
count = 0
result = ''
while i < len_board:
    if board[i] == '.':
        if count % 2 == 0:
            while count >= 4:
                result += 'AAAA'
                count -= 4
            if count != 0:
                result += 'BB'
                count -= 2
            result += '.'

        else:
            result = -1
            break
    else:
        count += 1
    i += 1
else:
    result = result[:len_board-1]
print(result)
