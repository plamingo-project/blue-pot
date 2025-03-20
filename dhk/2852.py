# 2852 NBA 농구(S3)
# 수학 계산 -> 그대로 구현하지말고 48분 기준으로 득점 시간들만 계산하면 될듯
# 득점 <-> 다음 득점까지의 시간 계산
# winner 확인
# 초 단위로 배열에 넣으면 ? 48 * 60 크기 (충분히 가능..?)
# [0,0,0,1,1,1,1,2,2,2] => 초 단위로 이기고 있는 팀 구하기
# 효율적이진 않지만 시간초과 발생할 일은 없음
# 각 칸은 1초 -> 이후 count로 새어주기만 하면 됨

# 초 단위로 초기화
timer = [0 for _ in range(48*60)]
# 0 ~ 2880초 (48분)

one_score = 0
two_score = 0

n = int(input())
for _ in range(n):
    team, time = input().split()
    if team == "1":
        one_score += 1
    else:
        two_score += 1

    # cal time
    m, s = time.split(":")
    idx = (int(m) * 60) + int(s)

    if one_score == two_score:
        # 동점이면 득점 시간 기준으로 시간 모두 0으로
        for i in range(idx, len(timer)):
            timer[i] = 0
    elif one_score > two_score:
        for i in range(idx, len(timer)):
            timer[i] = 1
    else:
        for i in range(idx, len(timer)):
            timer[i] = 2
# one
one_m = timer.count(1) // 60
one_s = timer.count(1) % 60
one_ret = ""
if one_m < 10:
    one_ret += "0"

one_ret += str(one_m)

one_ret += ":"

if one_s < 10:
    one_ret += "0"

one_ret += str(one_s)


two_m = timer.count(2) // 60
two_s = timer.count(2) % 60

two_ret = ""
if two_m < 10:
    two_ret += "0"
two_ret += str(two_m)

two_ret += ":"

if two_s < 10:
    two_ret += "0"
two_ret += str(two_s)

print(one_ret)
print(two_ret)
