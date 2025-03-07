# 4375(S3) - 1

# 2와 5로 나눠지지않는 정수 n
# 각 자릿수가 모두 1로만 이루어진 n의 배수 찾기

while True:
    try:
        target = 1
        k = 1
        n = int(input())
        while True:
            if target % n == 0:
                print(len(str(target)))
                break
            else:
                target += (k * 10)
                k *= 10

    except:
        break
