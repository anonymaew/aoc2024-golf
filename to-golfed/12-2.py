t = open(0).read()
w = t.count('\n')
f = []
for _ in range(w):
    f += [[0]*w]

for i in range(w):
    for j in range(w):
        c = t[i*(w+1)+j]
        no = None if i == 0 else t[(i-1)*(w+1)+j]
        ea = None if j == w-1 else t[i*(w+1)+j+1]
        so = None if i == w-1 else t[(i+1)*(w+1)+j]
        we = None if j == 0 else t[i*(w+1)+j-1]
        if (c != no) and (c != ea):
            f[i][j] += 1
        if (c != ea) and (c != so):
            f[i][j] += 1
        if (c != so) and (c != we):
            f[i][j] += 1
        if (c != we) and (c != no):
            f[i][j] += 1
        if (c == no != None) and (c == ea != None) and (c != t[(i-1)*(w+1)+j+1]):
            f[i][j] += 1
        if (c == ea != None) and (c == so != None) and (c != t[(i+1)*(w+1)+j+1]):
            f[i][j] += 1
        if (c == so != None) and (c == we != None) and (c != t[(i+1)*(w+1)+j-1]):
            f[i][j] += 1
        if (c == we != None) and (c == no != None) and (c != t[(i-1)*(w+1)+j-1]):
            f[i][j] += 1


def add_tup(i, j):
    return tuple(map(sum, zip(i, j)))


def calc(c, p):
    global t
    if t[p] != c:
        return (0, 0)
    t = t[:p] + "."+t[p+1:]
    res = (1, f[p//(w+1)][p % (w+1)])
    if (p//(w+1) > 0):
        res = add_tup(res, calc(c, p-w-1))
    if (p % (w+1) < w-1):
        res = add_tup(res, calc(c, p+1))
    if (p//(w+1) < w-1):
        res = add_tup(res, calc(c, p+w+1))
    if (p % (w+1) > 0):
        res = add_tup(res, calc(c, p-1))
    return res


s = 0
for i in range(w*w+w):
    if (i % (w+1) == w):
        continue
    if t[i] != ".":
        a, c = calc(t[i], i)
        s += a*c
print(s)
