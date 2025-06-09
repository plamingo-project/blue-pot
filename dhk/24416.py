# 24416 - 알고리즘 수업 피보나치 수 1 (B1)

# fib(n) {
#     if (n = 1 or n = 2)
#     then return 1;  # 코드1
#     else return (fib(n - 1) + fib(n - 2));
# }
# 피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.
ret_rec = 0
ret_dp = 0


def fib(n):
    global ret_rec
    ret_rec += 1
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }


def fibonacci(n):
    dp = [0 for _ in range(n)]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        global ret_dp
        ret_dp += 1
    return dp[n]


n = int(input())
fib(n)
fibonacci(n)
print(ret_rec, ret_dp)
