# 18258 큐2 (S4)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

queue = deque()

for _ in range(n):
    cmd = list(input().split())

    if cmd[0] == "push":
        queue.append(cmd[1])
        continue

    if cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
        continue

    if cmd[0] == "size":
        print(len(queue))
        continue

    if cmd[0] == "empty":
        print(0 if queue else 1)
        continue

    if cmd[0] == "front":
        print(queue[0] if queue else -1)
        continue

    if cmd[0] == "back":
        print(queue[-1] if queue else -1)
        continue
