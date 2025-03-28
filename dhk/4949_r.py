# 4949 균형잡힌 세상(S4) - 다시 풀기

bracket_a = "()"
bracket_b = "[]"
check = bracket_a + bracket_b

while True:
    text = input()
    if text == ".":
        break

    stack = []
    for c in text:
        if c in check:
            if stack:
                # check stack
                top = stack[-1]
                if top in bracket_a and c in bracket_a:
                    if top + c == "()":
                        stack.pop()
                        continue

                if top in bracket_b and c in bracket_b:
                    if top + c == "[]":
                        stack.pop()
                        continue

                stack.append(c)

            else:
                stack.append(c)
                # 순서 잘못된 경우
                if c in ")]":
                    break

    # print result
    print("no" if stack else "yes")
