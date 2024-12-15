
all = open(0).read()
table, others = all.split('\n\n')
w = (table.count('\n')+1)*2


def can_move(t, pos, dp):
    if t[pos+dp] == '.':
        return True
    if t[pos+dp] == '#':
        return False
    if abs(dp) > 1:
        if t[pos+dp] == '[':
            return can_move(t, pos+dp, dp) and can_move(t, pos+dp+1, dp)
        if t[pos+dp] == ']':
            return can_move(t, pos+dp, dp) and can_move(t, pos+dp-1, dp)
    return can_move(t, pos+dp, dp)


def moving(t, to_replace, pos, dp):
    if t[pos] == '.':
        t = t[:pos]+to_replace+t[pos+1:]
        return t
    if t[pos] == '#':
        if to_replace != '.':
            raise Error("heedor")
        return t
    if abs(dp) > 1:
        if t[pos+dp] == '[':
            # t = t[:pos+1]+'.'+t[pos+2:]
            t = moving(t, '.', pos+1+dp, dp)
        if t[pos+dp] == ']':
            # t = t[:pos-1]+'.'+t[pos:]
            t = moving(t, '.', pos-1+dp, dp)
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

double_wide_table_translate = {
    '#': "##",
    'O': "[]",
    '.': "..",
    '@': "@.",
    '\n': "\n",
}

t = ''.join([double_wide_table_translate[c] for c in table])
for c in others:
    if c in dps:
        t = move(t, dps[c])

s = 0
for i, c in enumerate(t):
    x = i % (w+1)
    y = i//(w+1)
    if c == "[":
        s += x+100*y
print(s)
