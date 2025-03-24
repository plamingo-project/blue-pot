# 4949 균형잡힌 세상(S4)

primary = "()"
secondary = "[]"
check = primary + secondary

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
                if top in primary and c in primary:
                    if top + c == "()":
                        stack.pop()
                        continue

                if top in secondary and c in secondary:
                    if top + c == "[]":
                        stack.pop()
                        continue

                stack.append(c)

            else:
                stack.append(c)
                if c in ")]":
                    break

    # print result
    print("no" if stack else "yes")
