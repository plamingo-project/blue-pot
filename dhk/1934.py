# 1934 - 최소공배수(B1)
# A,B의 최소 공배수 구하기
t = int(input())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


for _ in range(t):
    a, b = map(int, input().split())

    if a > b:
        tmp = gcd(a, b)
        print(a*b // tmp)
    else:
        tmp = gcd(b, a)
        print(a*b // tmp)
