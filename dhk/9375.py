# 9375번 - 패션왕 신해빈
T = int(input())

# desc
# 종류 1개만 입는 경우
# 조합해서 입는 경우

# solution
# each test case
for _ in range(T):
    # 테케별 리턴 값
    rst = 1
    # 의상 갯수
    n = int(input())
    # clothes -> dictionary
    d = {}
    for _ in range(n):
        v, k = map(str, input().split())
        if k in d.keys():
            d[k].append(v)
        else:
            d[k] = [v]

    # 의상 조합 개수 : (종류 개수+1) * (종류 개수 +1) ... -1 (모두 안입는 경우 제외)
    for k in d.keys():
        rst *= (len(d[k]) + 1)

    print(rst - 1)

# 점화식을 도출해내지 못하면 풀지 못함
