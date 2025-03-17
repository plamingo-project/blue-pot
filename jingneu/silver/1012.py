import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()


#인접해있는 배추 무리의 수

#q가 없어질 때, - 인접 +1

T = int(input())
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]


for _ in range(T):
    M, N, K = map(int, list(input().split(" ")))
    ans = 0
    arr = [[0]*N for _ in range(M)]
    cabbages = []
    
    for i in range(K):
        x, y = map(int, input().split(" "))
        arr[x][y] = 1
        cabbages.append([x, y])
    
    visited = [[False]*N for _ in range(M)]
    
    for x, y in cabbages:
        if visited[x][y]: continue
        
        q = deque()
        q.append([x, y])
        ans+=1
        visited[x][y] = True
        
        while len(q) != 0:
            curX, curY = q.popleft()
            for x, y in move:
                nextX = curX+x
                nextY = curY+y
                if 0<=nextX<M and 0<=nextY<N and not visited[nextX][nextY] and arr[nextX][nextY] == 1:
                    q.append([nextX, nextY])
                    visited[nextX][nextY] = True
        
    print(ans)