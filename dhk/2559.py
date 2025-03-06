# 2559 - 수열

# inputs
N, K = map(int, input().split())

numbers = list(map(int, input().split()))
# len(numbers) <= 100_000


# solution
# 슬라이딩 윈도우
current = sum(numbers[:K])
rst = current  # 최댓값 초기화

for i in range(1, N - K + 1):
    current = current - numbers[i-1] + numbers[i+K-1]  # 맨 앞 숫자 빼고, 새로운 숫자 추가
    rst = max(rst, current)

print(rst)

# 누적합
