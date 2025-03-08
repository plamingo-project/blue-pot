import sys
input = sys.stdin.readline

word = list(input().strip())

if word == list(reversed(word)):
    print(1)
else:print(0)