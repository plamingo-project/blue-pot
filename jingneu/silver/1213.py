import sys
input = lambda: sys.stdin.readline().strip()

# 팰린드롬 가능 ? 
# 문자열을 가지고 팰린드롬을 만들어라! 는 문제 ...

arr = list(input())

#팰린드롬 조건 : (start)짝수개만큼 가지고 있는 숫자 // 2 + (mid)남는 숫자 (무조건 길이 0 or 1) + (start reverse)

dic = {}

for word in arr:
    if not word in dic.keys():
        dic[word] = 1
    else:
        dic[word] += 1


def Solution():
    global dic
    start = []
    mid = [] #always len 0 or 1
    
    for key in sorted(dic.keys()):
        if dic[key]%2 == 0:
            start+=([key]*(dic[key]//2))
        if dic[key]%2 == 1:
            mid+=[key]
            start+=([key]*((dic[key]-1)//2))
            if len(mid) > 1:
                return "I'm Sorry Hansoo"
    
    newList = start+mid+list(reversed(start))
    return "".join(newList)
    
print(Solution())

#reversed 는 list_reversiterator type 을 반환, list처럼 쓰려면 list 로 변환 필요!