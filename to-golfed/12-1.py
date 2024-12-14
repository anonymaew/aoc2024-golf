
t = open(0).read()
w = t.count('\n')
f = [[2]+[1]*(w-2)+[2]]
for _ in range(w-2):
    f+= [[1]+[0]*(w-2)+[1]]
f +=[[2]+[1]*(w-2)+[2]]

for i in range(w):
    for j in range(w-1):
        if t[i*(w+1)+j] != t[i*(w+1)+j+1]:
            f[i][j] +=1
            f[i][j+1] +=1
        if t[j*(w+1)+i] != t[(j+1)*(w+1)+i]:
            f[j][i] += 1
            f[j+1][i] +=1

def add_tup(i,j):
    return tuple(map(sum,zip(i,j)))

def calc(c,p):
    global t
    if t[p]!=c:
        return (0,0)
    t = t[:p]+ "."+t[p+1:]
    res = (1,f[p//(w+1)][p%(w+1)])
    if (p//(w+1)>0):
        res = add_tup(res,calc(c,p-w-1))
    if (p%(w+1)<w-1):
        res = add_tup(res,calc(c,p+1))
    if (p//(w+1)<w-1):
        res = add_tup(res,calc(c,p+w+1))
    if (p%(w+1)>0):
        res = add_tup(res,calc(c,p-1))
    return res

s = 0
for i in range(w*w+w):
    if (i%(w+1)==w):
        continue
    if t[i]!=".":
        a,c = calc(t[i],i)
        s+= a*c
print(s)

