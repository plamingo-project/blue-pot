import sys
input = sys.stdin.readline

ans = [0]*26

S = list(input().strip())

#a 유니코드 -> 97 
#유니코드 - 97 


for i in S:
    temp = ord(i) - 97
    ans[ord(i) - 97] += 1


for i in ans:
    print(i, end=" ")