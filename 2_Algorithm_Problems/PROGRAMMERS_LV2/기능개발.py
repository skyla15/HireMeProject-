def solution(progresses, speeds):
    answer = []
    times = 1
    cnt = 0
    while progresses :
        if progresses[0] + speeds[0] * times >= 100 :
        # times를 통해 각각 각 기능들이 걸리는 시간을 구함 
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1 
        # 기능들 진행도가 100% 이상인 경우, pop 및 카운트 
        # times는 계속 같은 변수를 사용함으로 뒤의 작업들이 앞의 작업들보다 걸리는 시간이 작을 경우 
        # 이미 끝나있음. 따라서 앞의 작업보다 작업시간이 작은 작업들은 이 과정에서 같이 카운트가 됨 
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            times += 1      
      
    answer.append(cnt)
    # 마지막 요소까지 카운트가 될 경우, 마지막 요소는 루프에서 들어가지 않으므로 추가해줌 
    
    return answer
    
    
  #  입출력 예 :
  #  progresses	speeds	  return
  #  [93,30,55]	[1,30,5]	[2,1]
