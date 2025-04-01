# 15649 - N과 M(1) (S3)

# 1~ N까지 자연수 중에서 중복 없이 M개를 고른 수열
# from itertools import permutations as pm

# n, m = map(int, input().split())
# numbers = [i for i in range(1, n+1)]

# for i in pm(numbers, m):
#     print(*i)

# 백트래킹 풀이
def back():
    # m개 뽑은 경우
    if len(arr) == m:
        print(*arr, sep=" ")
        return

    # 재귀 시작될 때마다 i값은 초기화됨
    # 순차적으로 하나의 값을 뽑음.
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()


n, m = map(int, input().split())

arr = []

back()
