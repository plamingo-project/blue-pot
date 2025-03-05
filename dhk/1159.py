# 1159 농구 경기
import sys
input = sys.stdin.readline

N = int(input())
# 결과값은 set으로 저장(중복 제거)
rst = set()
names = [input().rstrip() for _ in range(N)]
for name in names:
    # 체크할 문자
    letter = name[0]
    if len(list(filter(lambda str: str[0] == letter, names))) >= 5:
        rst.add(letter)

print("".join(sorted(rst)) if len(rst) > 0 else "PREDAJA")

# 이미 체크한 letter를 저장해두고 중복 체크를 안하도록 수정할 수 있을 듯?
