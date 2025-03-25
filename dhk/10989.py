# 10989 수 정렬하기(B1) - 기초 연습
import sys
input = sys.stdin.readline

n = int(input())
# 각 숫자의 갯수 저장
ret = [0] * 10001
for _ in range(n):
    num = int(input())
    ret[num] += 1

for i in range(len(ret)):
    if ret[i] != 0:
        for j in range(ret[i]):
            print(i)
