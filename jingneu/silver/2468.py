import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]

max_rain = max(map(max, arr))


ans = 1
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]



for rain in range(1, max_rain+1):
    visited = [[False]*N for _ in range(N)]
    tempAns = 0
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and not visited[i][j]:
                tempAns+=1
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                
                # while len(q)!=0:
                while q:
                    curX, curY = q.popleft()
                    for x, y in move:
                        nextX = curX + x
                        nextY = curY + y
                        if 0<=nextX<N and 0<=nextY<N and arr[nextX][nextY] > rain and not visited[nextX][nextY]:
                            q.append((nextX, nextY))
                            visited[nextX][nextY] = True
    ans = max(ans, tempAns)
                            
print(ans)

#엣지케이스 연습 필요
# N은 2이상의 정수, 높이는 1이상의 정수.
# -> 아무 지역도 물에 잠기지 않을 수 있다. => 따라서 ans 기본 값을 1로 설정해야 한다. 
