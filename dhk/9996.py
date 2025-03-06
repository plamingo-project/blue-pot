# 9996 한국이 그리울 땐 서버에 접속하지

# 파일의 개수
N = int(input())
pattern = input()

# make prefix, suffix
prefix = ""
suffix = ""

for c in pattern:
    if c == "*":
        suffix = pattern[(pattern.index(c) + 1):]
        break
    else:
        prefix += c

# check prefix, suffix
# print(prefix)
# print(suffix)

for _ in range(N):
    target = input()
    if target.startswith(prefix) and target.endswith(suffix) and len(target) >= (len(suffix) + len(prefix)):
        print("DA")
    else:
        print("NE")


# 히든 테케 ->
# pattern : a*a
# case : a
# 대조해야하는 패턴의 총 길이 (* 제외 길이)보다 값이 작은 경우
# prefix, suffix가 일치하지만 만들 수 없음
