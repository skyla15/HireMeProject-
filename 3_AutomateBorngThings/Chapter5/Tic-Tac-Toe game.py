theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def gameManual():
    print('Move Guide....')
    print('*** * ***')
    print('* ' + '0' + '|' + '1' + '|' + '2' + ' *')
    print('* ' + '-+-+-' + ' *')
    print('* ' + '3' + '|' + '4' + '|' + '5' + ' *')
    print('* ' + '-+-+-' + ' *')
    print('* ' + '6' + '|' + '7' + '|' + '8' + ' *')
    print('*** * ***')
    print()


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def winnerCheck(board):
    if(
            board['top-L'] == board['top-M'] == board['top-R'] != ' ' or    # top horizontal
            board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ' or    # mid horizontal
            board['low-L'] == board['low-M'] == board['low-R'] != ' ' or    # low horizontal
            board['top-R'] == board['mid-R'] == board['low-R'] != ' ' or    # right vertical
            board['top-L'] == board['mid-L'] == board['low-L'] != ' ' or    # left vertical
            board['top-M'] == board['mid-M'] == board['low-M'] != ' ' or    # mid vertical
            board['top-L'] == board['mid-M'] == board['low-R'] != ' ' or    # diagonal \
            board['low-L'] == board['mid-M'] == board['top-R'] != ' '       # diagonal /
    ):
        return True
    else:
        return False


def updateBoard(turn):
    global theBoard
    print('Turn : ' + turn + '\nMove on which space?')
    move = int(input())
    while True:
        if move not in range(0, 9):
            move = int(input('Key Error, pick another space\n'))
        k = list(theBoard.keys())[move]
        if theBoard[k] != ' ':
            move = int(input('The space is already taken, pick another space\n'))
        else:
            theBoard[k] = turn
            break
    switchMark(turn)


def switchMark(turn):
    global theBoard
    if theBoard['top-L'] == theBoard['top-R'] == turn:
        theBoard['top-M'] = turn
        printBoard(theBoard)
    elif theBoard['mid-L'] == theBoard['mid-R'] == turn:
        theBoard['mid-M'] = turn
        printBoard(theBoard)
    elif theBoard['low-L'] == theBoard['low-R'] == turn:
        theBoard['low-M'] = turn
        printBoard(theBoard)
    elif theBoard['top-R'] == theBoard['low-R'] == turn:
        theBoard['mid-R'] = turn
        printBoard(theBoard)
    elif theBoard['top-L'] == theBoard['low-L'] == turn:
        theBoard['mid-L'] = turn
        printBoard(theBoard)
    elif theBoard['top-M'] == theBoard['low-M'] == turn:
        theBoard['mid-M'] = turn
        printBoard(theBoard)
    elif theBoard['top-L'] == theBoard['low-R'] == turn:
        theBoard['mid-M'] = turn
        printBoard(theBoard)
    elif theBoard['low-L'] == theBoard['top-R'] == turn:
        theBoard['mid-M'] = turn
        printBoard(theBoard)


def switchTurn(turn):
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    return turn


def main():
    global theBoard
    gameManual()
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)

        # 게임판 업데이트
        updateBoard(turn)

        # 승자 체크
        if winnerCheck(theBoard):
            print('winner dineer chicken dinner : ', turn)
            break

        # 턴 변경
        turn = switchTurn(turn)

if __name__ == '__main__':
    main()