# 4659 비밀번호 발음하기(S5)

# 구현 문제
# 1. 모음 (a,e,i,o,u) 포함할 것
# 2. 모음 3개 연속, 자음 3개 연속 안됨
# 3. ee, oo 제외 같은 글자가 연속으로 두번 오면 안됨

correct = " is acceptable."
wrong = " is not acceptable."

vowels = "aeiou"

while True:

    word = input()
    # vowels counter
    cnt = 0
    # 모음, 또는 자음 3회 반복 확인
    three = False
    # 연속 확인
    doubled = False

    stack = []
    # end
    if word == "end":
        exit()

    # solution
    # 1. 모음 포함할 것
    for i in vowels:
        cnt += word.count(i)

    # 2. 모음 3개 연속, 자음 3개 연속 안됨
    for c in word:
        if stack:
            # 3. 두 글자 연속 확인
            if stack[-1] == c:
                if c not in ["e", "o"]:
                    doubled = True
                    break
            stack.append(c)

            if len(stack) >= 3:
                # 3개씩 나눠서 조회
                tmp = stack[len(stack)-3:]
                v_cnt = 0
                c_cnt = 0
                for i in tmp:
                    if i in vowels:
                        v_cnt += 1
                    else:
                        c_cnt += 1
                if v_cnt >= 3 or c_cnt >= 3:
                    three = True
                    break

        else:
            stack.append(c)

    isCorrect = cnt > 0 and not doubled and not three
    # return part
    print("<", word, ">", correct if isCorrect else wrong, sep="")

# 너무 지저분하게 풀었음
# 3개 연속, 연속되는 것 어떻게 체크?
