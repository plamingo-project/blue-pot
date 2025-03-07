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
    # 홀수인 경우
    if len(target) % 2 != 0:
        pass
    # A,B의 개수가 짝수가 아닌 경우
    elif target.count("A") % 2 != 0 or target.count("B") % 2 != 0:
        pass
    else:
        target_stack = list(target)
        while len(target_stack) > 0:
            tmp = target_stack.pop()
            if len(stack) > 0:
                if stack[-1] == tmp:
                    lst = stack.pop()
                else:
                    stack.append(tmp)
            else:
                stack.append(tmp)
        if len(stack) == 0:
            rst += 1

print(rst)
