# 1068 트리(G5)

# 트리 -> 인접행렬로 만들기
import sys
sys.setrecursionlimit(10**6)

n = int(input())
nodes = list(map(int, input().split()))
remove_node = int(input())

adj = [[] for _ in range(n)]

# 루트가 반드시 0은 아니다
# 루트 찾기 / 인접 리스트 만들기
for child in range(n):
    parent = nodes[child]
    if parent != -1:
        adj[parent].append(child)
    else:
        root = child

ret = 0


def dfs(node):
    global ret
    # 삭제되는 노드라면 방문 안하고 없는 취급
    if node == remove_node:
        return

    # 자식이 없다면 -> leaf 노드임
    if not adj[node]:
        ret += 1
        return

    # 자식이 있는 경우 -> 삭제 노드만 있는 경우도 있으니 플래그로 탐색
    is_leaf = True
    for child in adj[node]:
        if child != remove_node:
            is_leaf = False
            # 삭제노드 외의 자식이 있다면 해당 자식으로 내려가서 탐색 시작
            dfs(child)

    if is_leaf:
        ret += 1


# 루트가 삭제된 경우
if root == remove_node:
    print(0)
else:
    # 루트에서부터 그래프 탐색 시작
    dfs(root)
    # 마지막 결과값 출력
    print(ret)
