# 2870(S4) 수학숙제

# stack에 쌓다가 문자열 나오면 stack에 있던 값 빼와서 숫자로 변환

ret = []

n = int(input())  # <= 100

numbers = "0123456789"

# inputs
for _ in range(n):
    stack = []
    word = input()
    for c in word:
        if c in numbers:
            stack.append(c)
        else:
            if stack:
                tmp = int("".join(stack))
                ret.append(tmp)
                stack = []
    if stack:
        tmp = int("".join(stack))
        ret.append(tmp)


print(*sorted(ret), sep="\n")
