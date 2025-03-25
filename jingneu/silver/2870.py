import sys
input = lambda: sys.stdin.readline().strip()

#숫자를 모두 찾은 후, 이 숫자를 오름차순으로 정리 
#숫자 앞에 0이 있으면 이를 생략

N = int(input())
arr = [input() for _ in range(N)]
digits = []

s = -1
e = -1

for word in arr:
    for i in range(len(word)):
        w = word[i]
        if w.isdigit():
            if s == -1:
                s = i
            else:
                continue
        else:
            if s != -1:
                e = i
                digits.append(int(word[s:e]))
                #init
                s = -1
                e = -1
                
    if s != -1:
        digits.append(int(word[s:]))
        #init
        s = -1
        e = -1
            
digits.sort()

for i in digits:
    print(i)


            