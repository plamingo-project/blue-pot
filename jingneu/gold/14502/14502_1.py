import sys
from collections import deque

input = sys.stdin.readline

#첫 접근 -> bfs로 전체 탐색하면서, 조건 (벽 세우기) + counting 하는 문제인 것 같다. 


#2에서 bfs 탐색 가능한 0 은 모두 2가 될 수 있다. 
#모든 0은 벽세우기 후보이다. 

#벽(i, j) 세운 후 막아지는 전파의 수는 어케 구하는가

N, M = map(int, input().split(" "))
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
arr = []
virus = []
outDegrees = [ [0, i, j] for j in range(M) for i in range(N)] #값, 행, 열


for i in range(N):
    temp = list(map(int, input().split(" ")))
    arr.append(temp)
    for j in range(M):
        if temp[j] == 2:
            virus.append([i, j])

#모든 2 -> bfs 탐색하면서, 전파가 발생할 때마다 진출자수 저장함 (누적) (visited 체크 x)
for x, y in virus:
    q = deque()
    q.append([x, y])
    
    while len(q) != 0:
        curx, cury = q.pop()
        for mx, my in move:
            nextx = curx+mx
            nexty = cury+my
            if(0<=nextx<N and 0<=nexty<M and arr[nextx][nexty] == 0):
                outDegrees[curx][cury][0] += 1
                q.append([nextx, nexty])
                
                
#진출차수가 큰 애들부터 정렬 
outDegrees.sort(reverse=True, key=lambda x: x[0])

#벽을 세웠을 때, 그 아래의 진출차수도 하나씩 깎음 

#전체 진출차수가 가장 작아질 때, 그 넓이를 구하시라


walls = 0
total = 0
kijun = 0

for cnt, i, j in outDegrees:
    if cnt == 0: break
    
    for mx, my in move:
        nextx = curx+mx
        nexty = cury+my
        if(0<=nextx<N and 0<=nexty<M and arr[nextx][nexty] == 0):
            
    
        
        
#이 때, 빈배열 수가 가장 커지는 상태를 저장하면서 이보다 커지는 값 있으면 갱신한다. 
