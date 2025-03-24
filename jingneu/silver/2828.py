import sys
input = lambda : sys.stdin.readline().strip()

#사과를 모두 담으려고 한다. 
#바구니 이동 거리의 최솟값

N, M = map(int, input().split(" "))
J = int(input()) #사과 개수
apples = [int(input()) for _ in range(J)]

baguni = 1 #start 만 저장
answer = 0

for loc in apples:
    if loc in range(baguni, baguni+M):
        continue
    elif loc < baguni:
        answer += baguni - loc
        baguni = loc
        
    elif loc >= baguni + M:
        answer += loc - M + 1 - baguni
        baguni = loc - M + 1

print(answer)