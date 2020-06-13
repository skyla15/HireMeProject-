def solution(board, moves):

    answer = 0
    dolls = []
    for i in range(len(moves)):
        moves[i] = moves[i] - 1

    for j in moves:
        # claw 위치 ( Board 의 열 인덱스 )
        if j >= len(board):
            # 보드의 행높이 벗어나면 탈출
            break
        for i in range(len(board)):
            if board[i][j] != 0:
                answer = checkDolls(board[i][j], dolls, answer)
                # Board의 열(j)에서 보드의 행(i)를 탑색, 가장 처음 것이 0이 아닐 경우, dolls 바구니에 doll원소 삽입
                board[i][j] = 0
                # 집어넣은 원소가 있던 자리는 0으로 채우고 행탐색 멈춤
                break
            else:
                pass

    return answer


def checkDolls(doll, dolls, answer):

    if dolls and dolls[-1] == doll :
        del dolls[-1]
        # 바구니 dolls 배열이 비어있지 않고, dolls 배열의 이전 원소가 현재 들어온 원소와 같다면 마지막 원소 삭제
        answer += 2
        # 삭제되는 인형은, 현재 들어오는 인형 + 이전에 있던 인형, 따라서 2개를 더해줌
    else :
        dolls.append(doll)
        # 바구니 배열(dolls)에 마지막 인형과 현재 들어온 인형이 같지 않다면 삽입

    return answer
    
if __name__ = '__main__' :
    test_case_board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    test_case_moves = [1,5,3,5,1,2,1,4]
    answer = solution(test_case_board, test_case_moves)
    # answer : 4
    
  
