import sys
from bisect import bisect_right
input = lambda: sys.stdin.readline().strip()

N, C = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

done = [] #탐색 마친 숫자
answer = {} #key - 빈도, val - num

#숫자를 빈도순대로 정렬
#count
for num in arr:
    if num in done:
        continue
    counts = arr.count(num)
    done.append(num)
    if answer.get(counts) == None:
        answer[counts] = [num]
    else:
        answer[counts].append(num)
        
#출력
sortedKey = sorted(answer.keys(), reverse=True)

ans = []

for key in sortedKey:
    for num in answer[key]:
        ans.extend([num]*key)

print(" ".join(map(str, ans)))