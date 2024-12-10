
map = open(0).read()
w = map.count('\n')

starts = [i for i, c in enumerate(map) if c == "0"]

map += " "*w


def explore(prevv, inow, m):
    print(inow, inow//(w+1), inow % (w+1))
    vnow = m[inow]
    if not vnow.isnumeric():
        return []
    vnow = int(vnow)
    if prevv + 1 != vnow:
        return []
    if vnow == 9:
        return [inow]
    m = m[:inow] + "#" + m[inow+1:]
    return (inow > (w+1))*(explore(vnow, inow-w-1, m)) + \
        (inow % (w+1) < w-1)*(explore(vnow, inow+1, m)) + \
        (inow//(w+1) < w-1)*(explore(vnow, inow+w+1, m)) + \
        (inow % (w+1) > 0)*(explore(vnow, inow-1, m))


s = 0
for start in starts:
    # print(start//(w+1), start % (w+1))
    score = explore(-1, start, map)
    s += len(set(score))
print(s)
