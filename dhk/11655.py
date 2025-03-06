# 11655 - ROT13

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = lowers.upper()

# ord 활용해서 lowers, uppers 사용없이 범위로 풀이 가능


def rot13(c):
    if c in lowers:
        computed = ord(c) + 13
        if computed > ord("z"):
            return chr(ord('a') - 1 + computed - ord("z"))
        else:
            return chr(computed)

    if c in uppers:
        computed = ord(c) + 13
        if computed > ord("Z"):
            return chr(ord('A') - 1 + computed - ord("Z"))
        else:
            return chr(computed)

    return c


# solution
S = input()
rst = ""
for c in S:
    rst += rot13(c)

print(rst)
