#한국이 그리울 땐 서버에 접속하지
import sys
input = sys.stdin.readline

N = int(input())
pattern = input().strip().split("*")
files = [input().strip() for _ in range(N)]

#무조건 file 이름은 별표를 기준으로 나뉜다. 
for file in files:
    if (file.startswith(pattern[0]) and file[len(pattern[0]):].endswith(pattern[1])):
        print("DA")
    else:
        print("NE")

#prefix 와 suffix 가 겹쳐서 조건이 성립하는 경우를 고려해야 한다. 
#startswith, endswith 는 겹치더라도 해당 패턴으로 시작 / 끝나면 True 를 반환한다.