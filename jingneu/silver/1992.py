#재귀

import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

def Solution(n, vlist):
    s = 0
    for l in vlist: s+= sum(l)
    
    
    if s == n**2: return '1'
    if s == 0: return '0'
    
    half = n//2
    temp = '('
    temp += Solution(half,[l[:half] for l in vlist[:half]])
    temp += Solution(half,[l[half:] for l in vlist[:half]])
    temp += Solution(half,[l[:half] for l in vlist[half:]])
    temp += Solution(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

print(Solution(N, arr))