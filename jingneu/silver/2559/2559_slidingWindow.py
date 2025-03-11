import sys
input = sys.stdin.readline
#슬라이딩 윈도우 ver
N, K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

temp = sum(arr[:K])
ans = temp

for i in range(K, N):
    temp = temp + arr[i] - arr[i-K]
    ans = max(ans, temp)

print(ans)