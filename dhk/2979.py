# 2979 - 트럭 주차

# 총 비용
A, B, C = map(int, input().split())

rst = 0
fees = [0, A, B, C]
# 1 ~ 100 -> 배열 ?
# 주차장 전체 시간
times = [0] * 101

for _ in range(3):
    # 시작 , 끝 시간
    start, end = map(int, input().split())
    for i in range(start+1, end+1):
        times[i] += 1

for t in times:
    rst += fees[t] * t

print(rst)
