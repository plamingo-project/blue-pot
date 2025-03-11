import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split(" "))
arr = list(map(int, input().strip().split(" ")))

#연속적인 며칠 동안의 온도의 합이 가장 큰가?
#N -> 온도를 측정한 전체 날짜의 수 
#K -> 합을 구하기 위한 연속적인 날짜의 수

#1. 누적합 구하기 
prefixSum = [0]*(N+1)

for i in range(1, N+1):
    prefixSum[i] = prefixSum[i-1] + arr[i-1]

#2. 누적합[i] - 누적합[i-k]
ans = -100*100000

for i in range(N+1):
    if(i-K<0): continue
    ans = max(ans, prefixSum[i] - prefixSum[i-K])

print(ans)

#음수 고려 안해서 틀렸었음