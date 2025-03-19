# DFS
깊이 우선 탐색

sudo code
```
DFS(u, adj)
u.visited = true
for each v ∈ adj[u]
if v.visited == false
DFS(v, adj)
```

1. 어떠한 정점 u를 방문처리하고 u에서 연결된 v지점을 탐색한다
2. 방문되어있지 않은 노드에 대해 재귀적으로 DFS를 호출한다

- 재귀 함수는 Stack으로 처리되기 때문에 DFS(가장 깊은 곳까지 방문) 역할을 수행할 수 있다.
