# 1629(S1) - 곱셈
a, b, c = map(int, input().split())
# (a * b ) %c = a % c * b % c


def go(a, b):
    # 기저 사례 - 가장 작은 값 (맨 마지막에 호출되는 함수의 종료 조건)
    if b == 1:
        return a % c
    # 재귀 호출(target의 절반)
    tmp = go(a, b // 2)  # 다음 재귀 호출 후 리턴 값을 저장
    tmp = (tmp * tmp) % c  # 다음 재귀함수의 리턴값을 제곱한 뒤 나머지 구하기
    # 홀수인 경우 한번 더 연산 (2^n * 2^n * 2)
    if (b % 2 == 1):
        tmp = (tmp * a) % c
    return tmp


# print(go(a, b))
