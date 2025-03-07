# 1940(S4) - 주몽
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

# solution

rst = 0
arr = list(map(int, input().split()))
arr.sort()

# 투 포인터 활용
# 재료들이 각각 고유한 번호이기 때문에 가능
start, end = 0, N-1
while start < end:
    tmp = arr[start] + arr[end]
    if tmp < M:
        start += 1
    elif tmp > M:
        end -= 1
    else:
        rst += 1
        start += 1
        end -= 1
print(rst)
