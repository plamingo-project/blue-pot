# 1620(S4) - 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())
d = {}
for i in range(1, N+1):
    pokemon = input()
    d[i] = pokemon
    d[pokemon] = i

# quiz
for i in range(M):
    query = input()
    if query.isnumeric():
        print(d[int(query)])
    else:
        print(d[query])

# dictionary 두개 활용해도 되는데, 그냥 하나에 다 넣어도 무관한 문제
