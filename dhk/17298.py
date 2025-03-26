# 17298 오큰수(G4)

# n < 1_000_000
n = int(input())

# 오큰수 찾아야하는 인덱스 담기
stack = []
# reversed
# ret -> print(*ret, sep=" ")
ret = [-1] * n


nums = list(map(int, input().split()))

# 1 ~ n-1
for i in range(n):
    # stack에 탐색해야할 idx 값이 있는 경우
    # 반복적으로 오큰수를 지정해준다.
    # 현재 탐색하는 값 (stack에 있는 index들보다 오른쪽의 값)이 큰 경우에는 오큰수로 지정해준다
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        ret[idx] = nums[i]
    stack.append(i)

print(*ret, sep=" ")

# 이중 루프 (시간초과)
# O(n**2)

# for i in range(0, n-1):
#     skip = False
#     current = nums[i]
#     for ni in range(i+1, n):
#         if nums[ni] > current:
#             print(nums[ni], end=" ")
#             skip = True
#             break
#     if not skip:
#         print(-1, end=" ")

# print(-1, end="")
