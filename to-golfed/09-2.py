s = []
filemode = True
nc = 0

normal = []
empty = []

for i in open(0).read()[:-1]:
    n = int(i)
    if filemode:
        normal += [(n, nc)]
        nc = nc+1
    else:
        empty += [[(n, None)]]
    filemode = not filemode

i = len(normal) - 1
while i >= 0:
    j = 0
    while j < i:
        diff = empty[j][-1][0]-normal[i][0]
        if diff >= 0:
            empty[j] = empty[j][:-1] + [(normal[i][0],normal[i][1]),(diff,None)]
            normal[i] = (normal[i][0], None)
            break;
        else:
            j += 1
    i -=1

k = 0
i = 0
for c in range(len(normal)):
    for _ in range(normal[c][0]):
        k += (normal[c][1] or 0) * i
        i += 1
    if c < len(empty)-1:
        for e in empty[c]:
            for _ in range(e[0]):
                k += (e[1] or 0) * i
                i += 1
print(k)
