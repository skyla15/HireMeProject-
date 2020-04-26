def solution(board, moves):

    dolls = []
    for i in range(len(moves)) :
        moves[i] = moves[i]-1


    print(len(board))
    for j in moves:
        # print('j : ', j)
        if j >= len(board) :
            # print('j out of range')
            break
        for i in range(len(board)):
            # print(i,j)
            if board[i][j] != 0:
                print(i, j, board[i][j])
                dolls.append(board[i][j])
                board[i][j] = 0
                print(dolls)
                break
            else :
                pass
    answer = checkDolls(dolls)
    return answer


def checkDolls(dolls):
    print(len(dolls))
    cnt = 0
    start = 0
    stop = 0
    isFirst = False
    for i in range(1, len(dolls)-1):
        if dolls[i - 1] == dolls[i] and isFirst == False:
            isFirst = True
            cnt += 1
            result = dolls[0:i] + dolls[i:]
        elif dolls[i-1] != dolls[i] :
            isFirst = False


    return cnt

print(solution(	[
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]],
    [1, 5, 3, 5, 1, 2, 1, 4]))

