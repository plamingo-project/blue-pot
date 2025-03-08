import sys
input = sys.stdin.readline

word = list(input().strip()) #strip 으로 공백 자르기 필수
wordLen = len(word)

stack = []

ans = 1

for i in range(wordLen):
    if wordLen%2 == 1 and i == wordLen//2:
        continue
    
    if i+1 <= wordLen//2:
        stack.append(word[i])
    else:
        compare = stack.pop()
        if(compare != word[i]):
            ans = 0
            break
        

print(ans)