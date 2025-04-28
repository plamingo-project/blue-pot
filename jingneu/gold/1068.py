import sys
from collections import defaultdict, deque

input = lambda : sys.stdin.readline().rstrip()
#노드 지웠을 때 남은 트리에서 리프 노드 개수 구하기 (노드 삭제 시 노드와 노드의 모든 자손이 트리에서 제거)
N = int(input())
indegree = list(map(int, input().split(" "))) #부모
graph = defaultdict(list) #outdegree
outdegree = [0]*N #-1 이라면 삭제된 노드

for i, v in enumerate(indegree):
    if v != -1:
        graph[v].append(i)
        outdegree[v]+=1

q = deque()

deleteNode = int(input())
q.append(deleteNode)
#부모를 찾아서 outdegree 삭제
if indegree[deleteNode] != -1:
    graph[indegree[deleteNode]].remove(deleteNode)

#bfs 탐색 하면서 자식 노드들 처리
while q:
    curNode = q.popleft()
    outdegree[curNode] = -1
    
    for nextNode in graph[curNode]:
        q.append(nextNode)
    graph[curNode] = []

ans = 0
#leaf 조건 : 부모 존재(indegree o), 자식 존재 x (graph length 0)
for key in range(N):
    if not graph[key] and outdegree[key] != -1:
        ans+=1

print(ans)