# 15989 1,2,3 더하기4 (G5)
# 정수 n이 주어졌을 때, 1,2,3의 합으로 나타내는 방법의 수
# n <= 10_000
# 1, 2, 3의 갯수로만 가지수 체크

# DP로 단계별로 저장하기
# dp[i] => i를 만드는 개수

# 모든 n에 대해서 1로만 구성된 방법이 하나는 존재함
import sys
input = sys.stdin.readline
dp = [1] * 10001

# 1로만 구성된 경우에서 2 추가되는 경우
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 1로만 구성된 경우에서 3 추가되는 경우
for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])


# 접근 방향은 정확했으나 메모이제이션을 활용하는 방법을 몰랐다
# 다양한 기출 문제를 풀면서 체화하는 게 중요한 것 같다
