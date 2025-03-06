# 2309
# for loop
arr = [int(input()) for _ in range(9)]
total = sum(arr)

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if total - arr[i] - arr[j] == 100:
            for k in sorted(arr):
                if k == arr[i] or k == arr[j]:
                    pass
                else:
                    print(k)
            exit()

# combinations 활용
# from itertools import combinations as cm

# arr = [int(input()) for _ in range(9)]

# for items in cm(arr, 7):
#     if sum(items) == 100:
#         for item in sorted(items):
#             print(item)
#         break
