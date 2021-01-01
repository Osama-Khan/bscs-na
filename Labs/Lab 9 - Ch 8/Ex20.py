lst = [
    [9, 6, 3, 16],
    [4, 15, 10, 5],
    [14, 1, 8, 11],
    [7, 12, 13, 2]
]


def rowCheck(s):
    for i in range(1, 4):
        if s != sum(lst[i]):
            return False
    return True


def colCheck(s):
    for i in range(0, 4):
        if s != (lst[0][i] + lst[1][i] + lst[2][i] + lst[3][i]):
            return False
    return True


def diagCheck(s):
    s1, s2 = 0, 0
    for i in range(0, 4):
        s1 += lst[i][i]
        s2 += lst[i][-(i + 1)]
    return s == s1 and s == s2


s = sum(lst[0])
isMagic = rowCheck(s) and colCheck(s) and diagCheck(s)
print(isMagic)
