import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(" "))

pocketmons = {}

for i in range(N):
    item = input().strip()
    num = str(i+1)
    pocketmons[num] = item
    pocketmons[item] = num

for i in range(M):
    question = input().strip()
    print(pocketmons.get(question))
        
#주의 -> list.index() 는 좀 느리다 (O(n))