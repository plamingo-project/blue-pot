import sys
input = lambda: sys.stdin.readline().strip()

#재료의 개수
N = int(input())
#갑옷 만드는데 필요한 수
M = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()


#두 개 합이 N이 될 수 있는 개수

p1 = 0
p2 = N-1

ans = 0
while p1<p2:
    if arr[p1]+arr[p2] == M:
        ans+=1
        p1+=1
        p2-=1 #같아지는 지점에서 p1+=1 했으니까 p2-=1 부터 탐색해야겠죠~~
    if arr[p1]+arr[p2] < M:
        p1+=1
    if arr[p1]+arr[p2] > M:
        p2-=1
        
print(ans)