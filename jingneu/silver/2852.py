import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = [input().split(" ") for _ in range(N)]

score = [0]*3
time = [[0, 0] for _ in range(3)] #분, 초
timer = [] #stack


for winner, t in arr:
    winner = int(winner)
    timeRange = list(map(int, t.split(":"))) #str
    score[winner]+=1
    looser = 3-winner
    
    #동점에서 득점한 경우
    if score[winner] == score[looser]+1:
        timer.append(timeRange)
        
    #동점이 되는 경우(지다가 동점)
    if score[winner] == score[looser]:
        if timer:
            startTime = timer.pop()
            time[looser][0] += (timeRange[0] - startTime[0])
            time[looser][1] += (timeRange[1] - startTime[1])
 
if timer:
    startTime = timer.pop()
    winner = 1
    if score[1]<score[2]:
        winner = 2

    time[winner][0] += (47 - startTime[0])
    time[winner][1] += (60 - startTime[1])
    
        

for i in range(1, 3):
    time[i][0] += time[i][1] // 60  # 초를 분으로 넘기기
    time[i][1] %= 60
    print("{:02d}:{:02d}".format(time[i][0], time[i][1]))