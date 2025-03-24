# 9012 괄호(S4)

n = int(input())
for _ in range(n):
    tc = input()

    stack = []
    for v in tc:
        if stack:
            # check stack[-1]
            top = stack[-1]
            if top == v:
                stack.append(v)
            else:
                stack.pop()

        else:
            stack.append(v)
            if v == ")":
                break

    print("NO" if stack else "YES")
