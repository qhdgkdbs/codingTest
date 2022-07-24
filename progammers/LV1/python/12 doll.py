# others
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer


# fail
def solution(board, moves):
    board =[[0,0,0,0,0], [0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves =[1,5,3,5,1,2,1,4]

    stack = []

    for i in moves:
        for idx, row in enumerate(board):
            # 열에 아이템이 있을 경우
            if row[i - 1] != 0:
                stack.append(row[i - 1])
                row[i - 1] = 0
                break
    print(stack)

    if len(stack) == 0:
        return 0
    if len(stack) == 1:
        return 0
    if len(stack) == 2:
        if stack[0] == stack[1]:
            return 2
        else:
            return 0
    if len(stack) == 3:
        if stack[0] == stack[1] or stack[0] == stack[2] or stack[1] == stack[2]:
            return 2
        if stack[0] == stack[1] == stack[2]:
            return 3

    idx = 0
    answer = 0

    while 1:
        if idx == len(stack) - 2:
            break
        if stack[idx] == stack[idx + 1]:
            print(stack[idx], stack[idx + 1])
            del stack[idx]
            del stack[idx]
            answer += 2
            idx = 0
        else:
            idx += 1

    return answer
