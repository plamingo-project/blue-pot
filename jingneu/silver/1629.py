import sys
input = lambda : sys.stdin.readline().strip()

A, B, C = map(int, input().split(" "))

#A^B % C

# = (A^B/2 * A^B/2) % C
# = (A^B/2%C) * (A^B/2%C) % C


atom = A % C


def double(b):
    if(b == 1):
        return atom
    
    solve = double(b//2)
    
    if (b % 2 == 0): #짝수일 때
        return solve * solve % C
        
    else: #홀수 일 때 
        return solve * solve * A % C
        
    
def solution():
    print(double(B))
    
    
solution()

# 2트 실패 .. 다시 풀기