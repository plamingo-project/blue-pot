# 3986(S4) - 좋은 단어

# 좋은 단어가 아닌 경우 -> Stack으로 쌍 맞추기
# ABAB BABA가 포함된 경우
# 단어 길이는 2 ~ 100,000
import sys
input = sys.stdin.readline

rst = 0

N = int(input())
for _ in range(N):
    stack = []
    target = input().rstrip()
    for i in range(len(target)):
        if stack:
            if stack[-1] == target[i]:
                stack.pop()
            else:
                stack.append(target[i])
        # stack is empty
        else:
            stack.append(target[i])
    # if stack is empty
    if not stack:
        rst += 1

print(rst)
# stack 하나로도 풀 수 있음
