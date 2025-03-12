import sys
input = sys.stdin.readline

cases = int(input().strip())

def Solution():
    N = int(input().strip())
    
    dic = {}
    for _ in range(N):
        temp = input().strip().split(" ")
        if temp[1] in dic:
            dic[temp[1]] += 1
        else:
            dic[temp[1]] = 1 
    
    #가능한 모든 조합의 수를 구하라 
    ans = 1
    for key in dic.keys():
        ans *= dic[key] + 1 #안입는 경우의 수도 포함
    
    print(ans - 1)


for i in range(cases):
    Solution()



    