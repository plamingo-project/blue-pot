# 15651 - N과 M(3) (S3)

# 같은 수를 여러 번 골라도 된다.

def go():
    if len(ret) == m:
        print(*ret, sep=" ")
        return

    for i in range(1, n+1):
        ret.append(i)
        go()
        ret.pop()


n, m = map(int, input().split())
ret = []

go()
