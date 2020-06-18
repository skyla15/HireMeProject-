# Finding the exit of the maze
# ############################
#    0 1 2 3 4 5 ( x )
# 0  x x x x x x
# 1  e o o o o x
# 2  x o x o x x
# 3  x x x o o o
# 4  x x x o x x
# 5  x x x x x x
#(y)
# ############################
# Basic Idea : 현재의 경로가 막혔을 경우 다시 선택할 수 있는 다른 경로들을 저장함
#              가장 최근의 갈림길로 돌아가 다른 곳을 찾음
# 1) DFS(스택) : 인접한 위치들 방문 후, 방문한 위치들에 인접한 위치들을 순서대로 찾음.
# 2) BFS(큐)  : 하나의 경로를 선해 끝까지 가고 막히면 새로운 경로 찾음
################################

# BFS 가정
# 시작 : 첫 위치 스택 삽입
# Step1 : 스택이 공백이 아닐 경우
#         - 위치를 끄냄 ( 현재위치 )
#         - 스택이 공백일 경우, 미로에 출구가 없믄 것
#         - 방문했다는 위치 등록
# Step2 : 현재 위치가 출구일 경우 탈락
#         - 아닐 경우, 상하좌우 이웃방 확인 후 벽이 아닐 경우 스택에 삽입 

from Queue import Queue

def isValidPos(x,y, map):
    if map[x][y] == '0'  or map[x][y] == 'x':
        return True
    return False

    # if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]) :
    #     return False
    # elif map[x][y] == '0' or map[x][y] == 'x' :
    #     return True


def BFS(start_coordinate, end_coordinate, map):
    s = Queue()
    s.enqueue(start_coordinate)
    step = 0

    while not s.isEmpty():
        here = s.dequeue()
        (x,y)=here

        if here == end_coordinate :
            return True
        else :
            map[x][y] = '.' # 방문 표시
            # DFS : 우좌하상 -> 상하좌우 순으로 꺼내서 확인
            # BFS : 우좌하상 -> 우좌상하 순으로
            # 꺼냈을 경우 가능한 경로가 있다면 일단 집어넣고 따라감
            if isValidPos(x, y + 1, map):
                s.enqueue( (x, y + 1) )
            if isValidPos(x, y - 1, map):
                s.enqueue( (x, y - 1) )
            if isValidPos(x + 1, y, map):
                s.enqueue( (x + 1, y) )
            if isValidPos(x - 1, y, map):
                s.enqueue( (x - 1, y) )
            step += 1

        for i in range(len(map[0])):
            for j in range(len(map)):
                print(map[i][j], end = ' ')
            print()

        print('status : ', s.q)
        print('steps: ', step)
        print()

    return False # While 문에서 True 반환 못한 경우 탐색 실패


if __name__ == '__main__' :

    map = [ [ '1', '1', '1', '1', '1', '1'],
            [ 'e', '0', '0', '0', '0', '1'],
            [ '1', '0', '1', '0', '1', '1'],
            [ '1', '1', '1', '0', '0', 'x'],
            [ '1', '1', '1', '0', '1', '1'],
            [ '1', '1', '1', '1', '1', '1'],]

    result = BFS((1,0), (3,5), map)

    if result :
        print('미로 탐색 성공')
    else :
        print('미로 탐색 실패')


