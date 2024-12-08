from collections import defaultdict
from itertools import combinations

table = []
antennas = defaultdict(list)
antinodes = set()

for i,l in enumerate(open(0).readlines()):
    table += [l]
    for j,c in enumerate(l[:-1]):
        if c!='.':
            antennas[c] += [(i,j)]
w=len(table)
for k in antennas:
    l = antennas[k]
    if (len(l)<2):
        continue
    for pair in combinations(l,2):
        diff = (pair[1][0]-pair[0][0],pair[1][1]-pair[0][1])
        ant1,ant2 = pair[0],pair[1]
        while True:
            if 0<=ant1[0]<w and 0<=ant1[1]<w:
                antinodes |= set([ant1[0]+ant1[1]*w])
            else:
                break
            ant1 = (ant1[0]-diff[0],ant1[1]-diff[1])
        while True:
            if 0<=ant2[0]<w and 0<=ant2[1]<w:
                antinodes |= set([ant2[0]+ant2[1]*w])
            else:
                break
            ant2 = (ant2[0]+diff[0],ant2[1]+diff[1])
print(len(antinodes))
