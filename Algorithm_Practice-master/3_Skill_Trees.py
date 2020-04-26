# 문제 접근 방법
# 1) 주어진 Skill Trees에서 스킬들의 순서가 정해져있는 스킬들이 존재한다면 
# 2) 해당 스킬들을 따로 리스크에 저장 
# 3) 주어진 스킬트리와 따로 리스트에 저장한 스킬들의 순서들은 순서가 같아야함 
# 4) 두 개의 리스트를 검사하여 순서가 맞지않는 요소가 있다면 False 반환 
def solution(skill, skill_trees ) :
    answer = 0

    for skill_tree in skill_trees :
        a = [] 
        flg = True
        # 주어진 스킬트리들이 순서 제약을 따랐는 지 확인하기 위함 

        for i in range(len(skill_tree)) :
            if skill_tree[i] in skill :
                a.append(skill_tree[i])
        # 주어진 Skill에 있는 스킬들(순서 제약이 있는 스킬들)을 따로 리스트에 저장 

        for j in range(len(a)) :
            if a[j] != skill[j] :
                flg = False
        # 따로 저장한 스킬과 주어진 스킬트리 비교 

        if flg == True :
            answer += 1
        # 순서가 맞다면 answer+1

    return answer
