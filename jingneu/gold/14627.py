import sys
input = lambda: sys.stdin.readline().rstrip()

S, C = map(int, input().split(" "))
#남은 파 양 구하기
#하나의 파닭에 하나 이상의 파가 들어가면 안됨 
#파의 양은 최대로

onions = [int(input()) for _ in range(S)]
onions.sort()

s = 1
e = onions[-1]
amount = -1


while s<=e:
    m = (s+e)//2
    total = sum([onion // m for onion in onions])
    if total >= C:
        s = m+1
        amount = max(amount, m)
    else:
        e = m-1


total = sum(onions)

print(total - (C*amount))