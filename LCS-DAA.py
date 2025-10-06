def LRS(s: str):
    n = len(s)
    c = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                c[i][j] = 1 + c[i - 1][j - 1]
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    i, j = n, n
    lrs = []
    while i > 0 and j > 0:
        if s[i - 1] == s[j - 1] and i != j:
            lrs.append(s[i - 1])
            i -= 1
            j -= 1
        elif c[i - 1][j] >= c[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lrs.reverse()
    return c[n][n], ''.join(lrs)

s = "AABEBCDD"
lrs_length, lrs_string = LRS(s)
print("LRS Length:", lrs_length)
print("LRS:", lrs_string)


