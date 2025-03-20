# 10709 기상캐스터(S5)
# 남북 방향 -> H (세로)
# 동서 방향 -> W (가로)

h, w = map(int, input().split())

m = []
check_col = []
for _ in range(h):
    row = input()
    tmp = []
    for a in row:
        if a == "c":
            tmp.append(0)
        else:
            tmp.append(-1)
    m.append(tmp)

for j in range(h):
    if 0 in m[j]:
        check_col.append(j)

# 구름 움직이기

for j in range(h):
    # 구름이 있는 경우에만 확인
    if j in check_col:
        # row 탐색
        for i in range(w):
            if m[j][i] == 0:
                continue
            if m[j][i] == -1:
                # 왼쪽에 구름 있는지 확인
                # 맨 왼쪽이면 continue
                if i == 0:
                    continue
                tmp = 1
                while i - tmp >= 0:
                    if m[j][i-tmp] == 0:
                        m[j][i] = tmp
                        break
                    else:
                        tmp += 1


for j in range(h):
    print(*m[j], sep=" ")
