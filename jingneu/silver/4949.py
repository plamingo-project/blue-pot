#괄호 짝 -> 스택 아닐까?

import sys
input = sys.stdin.readline

while True:
    tc = list(input())
    if tc[0] == ".":
        break
    
    ans = 'yes'
    stack = []
    
    # 왼쪽 -> start, stack 에 넣기 
    # 오른쪽 -> stack 에서 pop 후 비교 (비교 불가 시 no)
    for word in tc:
        if word == '(' or word == '[':
            stack.append(word)
        elif (word == ')' or word == ']') and not stack:
            ans = 'no'
            break
        elif word == ')':
            peek = stack.pop()
            if peek != '(':
                ans = 'no'
                break
        elif word == ']':
            peek = stack.pop()
            if peek != '[':
                ans = 'no'
                break

    #비교가 끝났는데도 stack 이 남아있으면 no
    if stack:
        ans = 'no'
        
    print(ans)