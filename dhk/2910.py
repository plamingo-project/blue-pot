# 2910 빈도정렬(S3) (구현, hashmap 문제?)

n, c = input().split()
values = list(input().split())

ret = []

store = {}


for value in values:

    if value not in ret:
        ret.append(value)

    if value in store.keys():
        store[value] += 1
    else:
        store[value] = 1

ret.sort(key=lambda x: store[x], reverse=True)

for element in ret:
    for _ in range(store[element]):
        print(element, end=" ")
