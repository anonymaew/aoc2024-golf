
all = open(0).read()
table, others = all.split('\n\n')
w = table.count('\n')+1


def can_move(t, pos, dp):
    if t[pos+dp] == '.':
        return True
    if t[pos+dp] == '#':
        return False
    return can_move(t, pos+dp, dp)


def moving(t, to_replace, pos, dp):
    if t[pos] == '.':
        # t[pos] = to_replace
        t = t[:pos]+to_replace+t[pos+1:]
        return t
    if t[pos] == '#':
        if to_replace != '.':
            raise Error("heedor")
        return t
    tmp = t[pos]
    t = t[:pos]+to_replace+t[pos+1:]
    return moving(t, tmp, pos+dp, dp)


def move(t, dp):
    pos = t.index('@')
    if can_move(t, pos, dp):
        t = moving(t, '.', pos, dp)
    return t


dps = {
    '^': -w-1,
    '>': 1,
    'v': w+1,
    '<': -1,
}


t = table[:]
for c in others:
    if c in dps:
        t = move(t, dps[c])

s = 0
for i, c in enumerate(t):
    x = i % (w+1)
    y = i//(w+1)
    if c == "O":
        s += x+100*y
print(s)
