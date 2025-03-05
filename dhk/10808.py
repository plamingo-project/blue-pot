# 10808 알파벳 개수

S = input()
candidats = "abcdefghijklmnopqrstuvwxyz"

for a in candidats:
    print(S.count(a), end=" ")
