# 15650 - N과 M(2) (S3)

def backtracking():
    # 종료 조건
    if len(ret) == m:
        print(*ret, sep=" ")
        return

    # 종료 조건이 아닌 경우 -> 자식 노드 탐색
    for i in range(1, n+1):
        if i not in ret:
            # 배열에 값이 있는 경우
            if ret:
                if ret[-1] < i:
                    # 오름차순인 경우에만 원소 추가 및 백트래킹 재귀호출
                    ret.append(i)
                    backtracking()
                    ret.pop()
            # 배열에 값이 없는 경우
            else:
                ret.append(i)
                backtracking()
                ret.pop()


ret = []
n, m = map(int, input().split())

backtracking()
