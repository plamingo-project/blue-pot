import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

#선끼리 교차하지 않으며
#각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을 수 있다면
# => 좋은 단어

words = [input() for _ in range(N)]


def Solution(word):
    stack = []
    for w in word:
        if len(stack)!=0 and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    return len(stack) == 0

ans = 0

for word in words:
    if len(word)%2 != 0:
        continue
    if Solution(list(word)): 
        ans+=1

print(ans)


#스택을 생각하지 못했어서 처음에 생각이 안났었음
#스택으로 풀 수 있는 유형들 외우는 것이 좋을듯