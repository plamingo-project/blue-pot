import sys
input = sys.stdin.readline

N = int(input().strip())

arr = []


#첫 글자가 같은 선수 5명을 선발 
#5명보다 적으면 기권 
#뽑을 수 있는 성의 첫 글자를 모두 구해라
ans = [0]*26
ansStr = []
# ans = [[ord(alphabet[i])] for i in range(26)]

for i in range(N):
    arr.append(input().strip())


for name in arr:
    ans[ord(name[0]) - ord("a")]+=1

    
for i in range(26):
    if(ans[i] >= 5):
        ansStr.append(chr(i+ord("a")))



if(len(ansStr) == 0):
    print("PREDAJA")
else:
    print("".join(ansStr))