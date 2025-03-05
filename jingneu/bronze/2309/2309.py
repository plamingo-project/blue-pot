import sys
input = sys.stdin.readline

arr = []
total = 0
for i in range(9):
    temp = int(input())
    arr.append(temp)
    total+=temp

a = total - 100

#오름차 정렬
arr.sort()

#합이 a 인 두 인덱스를 고른다. r 은 무조건 r<l
r, l = 0, 8

while (r<l):
    temp = arr[r]+arr[l]
    if(temp > a):
        l-=1
    if(temp < a):
        r+=1
    if(temp == a):
        break

for i in range(9):
    if not (i == r or i == l):
        print(arr[i])