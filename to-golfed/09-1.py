s = []
filemode = True
nc = 0
for i in open(0).read()[:-1]:
    n = int(i)
    if filemode:
        s += [(n, nc)]
        nc = nc+1
    else:
        s += [(n, None)]
    filemode = not filemode

head,tail = 1,len(s)//2*2

while head < tail:
    diff = s[head][0] - s[tail][0]
    if diff > 0:
        s = s[:head] + [(s[tail][0],s[tail][1]),(diff,None)]  + s[head+1:tail]
        head += 1; tail -= 1
    elif diff == 0:
        s = s[:head] + [(s[tail][0],s[tail][1])]  + s[head+1:tail]
        head += 2; tail -= 2
    else:
        s = s[:head] + [(s[head][0],s[tail][1])] + s[head+1:tail] + [(-diff, s[tail][1])]
        head +=2

k = 0
i = 0
for p in s:
    for _ in range(p[0]):
        k += p[1] * i
        i += 1
print(k)
