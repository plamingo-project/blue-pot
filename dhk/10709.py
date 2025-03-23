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

# 문자열 순회하기
# 구름 있을 때마다 tmp값 초기화해서 거리 +1 하며
# tmp값을 배열에 넣어주면 됨 (몇 분후 구름이 오는가)

# 이전 값이 -1이 아니고 해당 값이 0이 아니면 tmp값 삽입
# 왜 이전 값만 확인하면 되나요?
# 왼쪽부터 순차적으로 구름이 지나가는데, 이미 구름이 떴던 곳이면 tmp 값이 들어가서
# -1이 아닙니다.
# 이전 인덱스가 -1이라는 건 왼쪽에 구름이 없다는 뜻입니다.
# list[i-1] != -1 and list[i] != 0
