# 2828 사과 담기 게임(S5)
# 배열

n, m = map(int, input().split())
# 떨어지는 사과 개수
j = int(input())

# 이동 거리
ret = 0

basket = []
for i in range(1, m+1):
    # 1 ~ m
    basket.append(i)

for _ in range(j):
    drop_pos = int(input())
    # 떨어지는 위치가 현재 basket 범위 내라면 이동 x
    if drop_pos in basket:
        continue
    # 마지막 값보다 크면 우측으로 이동
    if drop_pos > basket[-1]:
        while drop_pos not in basket:
            for i in range(m):
                basket[i] += 1
            ret += 1
    else:
        while drop_pos not in basket:
            for i in range(m):
                basket[i] -= 1
            ret += 1

print(ret)
