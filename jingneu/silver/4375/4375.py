import sys
input = lambda: sys.stdin.readline().strip()
arr = []

while True:
    T = input()
    if not T: break
    
    arr.append(int(T))


flag = 1 #1, 10, 100 .... 
memo = [0]*len(arr) #자리수마다 나머지를 누적
ans = [0]*len(arr) #최종 자리수 저장

while True:
    if memo == [-1]*len(arr): break #종료 조건 설정
    
    for i in range(len(arr)):
        if memo[i] == -1: continue
        
        memo[i]+=flag%arr[i] #나머지를 누적
        if memo[i] % arr[i] == 0:
            ans[i] = len(str(flag))
            memo[i] = -1
    flag*=10

print("\n".join(map(str, ans)))

#한번에 풀면 시간 더 줄여질 줄 알고 ... 시간복잡도 계산 공부 필요