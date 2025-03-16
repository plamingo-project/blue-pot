import sys
input = lambda: sys.stdin.readline().strip()
arr = []

while True:
    T = input()
    if not T: break
    
    T = int(T)
    flag = 1
    cur = 1
    
    while True:
        if cur%T == 0:
            print(len(str(flag)))
            break
        flag *= 10
        cur += flag