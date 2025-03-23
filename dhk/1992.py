# 1992 쿼드트리(S1)
# recursive -> 압축하기
# 분할정복 문제 익히기
# 각 영역 나누기 -> 재귀로 처리
# (0)

# 패턴 분석 -> recursive 시작할 때 반드시 괄호 시작, recursive 이후 반드시 괄호 닫기


n = int(input())

mat = []

for _ in range(n):
    row = input()
    tmp = []
    for c in row:
        tmp.append(c)
    mat.append(tmp)

ret = []
# 분할정복 문제 (하나의 지점을 기준으로 다른 값이 나오면 4분할 필요하다는 뜻)


def go(y, x, n):
    # 기준점
    tmp = mat[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            # 다른 값이 나온다면 4분할해야함
            # 4분할 방면은 어떻게 나누나?
            # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 왼쪽 위 -> n개 기준이므로 i ~ n//2 단위로 분류하면됨
            if mat[i][j] != tmp:
                ret.append("(")
                # 왼쪽 위
                go(y, x, n//2)
                # 오른쪽 위
                go(y, x+n//2, n//2)
                # 왼쪽 아래
                go(y+n//2, x, n//2)
                # 오른쪽 아래
                go(y+n//2, x+n//2, n//2)
                ret.append(")")
                return
    ret.append(tmp)


go(0, 0, n)
print(*ret, sep="")
