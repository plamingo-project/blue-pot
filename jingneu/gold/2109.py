import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
#하루 최대 한 곳, 가장 많은 돈 벌 수 있도록 순회 강연
arr = [list(map(int, input().split(" "))) for _ in range(n)]
days = [0]*10001 #i일에 벌 수 있는 최대 값 (나중에 sum)

#정렬 -> 1순위 : d 값이 작은 순서부터, (큰 것부터 고르다가 -> d -1 >0 이면 
# 그 아래거도 선택) 2순위: p 값이 큰 순서부터 

#1. 정렬
arr.sort(key=lambda x: (-x[0], x[1])) #큰 것부터, 가장 마감기한 촉박한 것부터


for pay, day in arr:
    if days[day] == 0:
        days[day] = pay
    
    else:
        available = day
        #그 다음 빈 칸을 찾아야함
        while True:
            available -= 1
            if available == 0:
                break
            if days[available] == 0:
                days[available] = pay
                break


print(sum(days))