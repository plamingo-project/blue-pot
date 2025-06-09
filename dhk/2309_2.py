# get data (난쟁이 키)
from itertools import combinations as cm

arr = [int(input()) for _ in range(9)]

for c in cm(arr, 7):
    if sum(c) == 100:
        for i in sorted(c):
            print(i)
        break
