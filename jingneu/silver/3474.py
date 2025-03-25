import sys
input = lambda: sys.stdin.readline().strip()

T = int(input())
arr = [int(input()) for _ in range(T)]

#N! = N * N-1 * N-2 * N-3 * ..... 2 * 1
#N! = N*(N-1)!

# 10 = 2*5 
# N! 안의 2, 5의 개수를 구하고 그 중 작은 것이 답이 된다.
# => 5의 개수를 구하자.

def Solution(N):
    cnt = 0
    i = 5
    while i<= N:
        cnt+= N//i
        i*=5
    return cnt
    
for num in arr:
    print(Solution(num))