import sys
input = sys.stdin.readline

A, B, C = map(int, input().split(" "))
charge = [0, A, B, C]
arr = []

start, end = [100, 0]

for i in range(3):
    s, e = map(int, input().split(" "))
    arr.append([s, e])
    
    start = min(start, s)
    end = max(end, e)
    
ans = 0

time = start

while True:
    
    if(time > end): break
    
    cnt = 0
    for s, e in arr:
        if(time in range(s, e)):
            cnt+=1

    ans += charge[cnt] * cnt
    time += 1
    
print(ans)