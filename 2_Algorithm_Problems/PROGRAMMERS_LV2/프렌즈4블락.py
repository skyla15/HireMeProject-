import pprint
from collections import deque
total = 0

# 다른 방법 : board를 Transpose해서 계산할 경우, 행별로 계산하면 되므로 더 간단하고 빠르게 셀 수 있을 듯
def masking(board, mask):
    global total
    for i in range(len(board) - 1):  # 현재 줄
        board[i] = list(board[i])
        board[i + 1] = list(board[i + 1])
        for j in range(0, len(board[0]) - 1):
            # 4개가 뭉쳐있으면서 한 번 스캔하였던 곳이 아니라면
            if ( board[i][j] == board[i+1][j] == board[i][j + 1] == board[i+1][j+1] ) and ( board[i][j] != 0 ) :
                mask[i][j] = mask[i][j + 1] = mask[i + 1][j] = mask[i + 1][j + 1] = 1
        total = total + mask[i].count(1)
    total = total + mask[len(board) - 1].count(1) # 마지막 줄

##### 출력 테스트
    print('==============================')
    print('total : ', total)
    for i in range(len(mask)):
        print(board[i], mask[i], sep='\t\t')
    print('==============================')

    is_dropped = drop(board, mask)
    if is_dropped:
        masking(board, mask)

    return total


def drop(board, mask):
    d = deque()
    drop_flag = False               # 블록들이 삭제되서 떨어졌다면 True
    for j in range(len(board[0])):
        for i in range(len(board)):
            if mask[i][j] == 0:     # 삭제되는 원소가 아니고 스캔이 되었다면 덱에 저장
               d.append(board[i][j])
               board[i][j] = 0      # 스캔한 원소 -> 0
            if mask[i][j] == 1:     # 터지는 블록들 카운트 하였으므로 mask -> 0,
                board[i][j] = 0
                mask[i][j] = 0
                drop_flag = True    # 마스킹 된 부분 확인 , flag = True
        # 보드 재조립
        for k in range(len(board) - 1, -1, -1):
            if len(d) != 0:
                board[k][j] = d.pop()
    print('drop flag : ', drop_flag)
    return drop_flag

def solution(m, n, board):
    mask = [[0 for x in range(n)] for y in range(m)]
    return masking(board, mask)

def main():
    board = ['CCBDET',
             'AATADE',
             'AAATBF',
             'CCBBTF']
    n = len(board[0])
    m = len(board)
    solution(m, n, board)

main()



### 내가 생각한거 그대로 구현하신 분

# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
#                 pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)
#
#
# def solution(m, n, board):
#     count = 0
#     b = list(map(list, zip(*board)))  # 행열 바꿔치기
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop