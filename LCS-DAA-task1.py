X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"
rows = len(X) + 1
cols = len(Y) + 1


c = [[{'val': 0, 'dir': 'h'} for _ in range(cols)] for _ in range(rows)]


for i in range(1, rows):
    for j in range(1, cols):
        if X[i - 1] == Y[j - 1]:
            c[i][j]['val'] = c[i - 1][j - 1]['val'] + 1
            c[i][j]['dir'] = 'd'  # diagonal
        else:
            if c[i - 1][j]['val'] >= c[i][j - 1]['val']:
                c[i][j]['val'] = c[i - 1][j]['val']
                c[i][j]['dir'] = 'u'  # up
            else:
                c[i][j]['val'] = c[i][j - 1]['val']
                c[i][j]['dir'] = 's'  # side (left)


print("Cost Matrix (Value and Direction):")
for row in c:
    print([(cell['val'], cell['dir']) for cell in row])


lcs_str = []
i, j = rows - 1, cols - 1


while i > 0 and j > 0:
    if c[i][j]['dir'] == 'd':
        lcs_str.append(X[i - 1])
        i -= 1
        j -= 1
    elif c[i][j]['dir'] == 'u':
        i -= 1
    else:
        j -= 1


lcs_str.reverse()
lcs_length = c[rows - 1][cols - 1]['val']
lcs_string = ''.join(lcs_str)


print("\nFinal LCS Length:", lcs_length)
print("LCS:", lcs_string)