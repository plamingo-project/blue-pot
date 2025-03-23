import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

M, N, K = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(K)]

spaces = 0 #0은 될수 없다. 
extents = [] #넓이 모음

graph = [[0]*M for _ in range(N)]
#1. 색칠하기
for x1, y1, x2, y2 in arr: 
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

#2. 탐색하기 
q = deque()

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = graph[:]


for x in range(N):
    for y in range(M):
        if visited[x][y] == 0:
            spaces+=1
            q.append([x, y])
            visited[x][y] = 1
            tempExtent = 1
            
            while q:
                curX, curY = q.popleft()
                
                for mx, my in move:
                    nextX = curX+mx
                    nextY = curY+my
                    if 0<=nextX<N and 0<=nextY<M and visited[nextX][nextY] == 0:
                        tempExtent+=1
                        visited[nextX][nextY] = 1
                        q.append([nextX, nextY])

            extents.append(tempExtent)

extents.sort()

print(spaces)
print(" ".join(list(map(str, extents))))