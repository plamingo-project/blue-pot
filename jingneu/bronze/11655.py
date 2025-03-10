import sys
input = sys.stdin.readline


def ROT(word):
    #숫자 or 공백이면 그대로 반환
    if(word.isdigit() or word == " "):
        return word
    
    #대소문자에 따른 기준 세우기
    isUp = word.isupper()
    standard = ord("a")
    if(isUp): standard = ord("A")
    

    if(ord(word) >= standard+13):
        return chr(ord(word) - 13)
    else:
        return chr(ord(word) + 13)


arr = list(input().rstrip())

for word in arr:
    print(ROT(word), end="")