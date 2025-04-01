# 13241 - 최소공배수(S5)
# 유클리드 호제법 (최대공약수 구하기)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


A, B = map(int, input().split())

if A > B:
    print(abs(A*B) // gcd(A, B))
else:
    print(abs(A*B) // gcd(B, A))
