import re
qs = [0, 0, 0, 0]
for line in open(0).readlines():
    pos = list(map(int, re.findall(r'p=(\d+),(\d+)', line)[0]))
    vel = list(map(int, re.findall(r'v=(-?\d+),(-?\d+)', line)[0]))
    lastpos = [(pos[0]+100*vel[0]) % 101, (pos[1]+100*vel[1]) % 103]
    if lastpos[0] == 50 or lastpos[1] == 51:
        continue
    qs[(lastpos[1]//52)*2+lastpos[0]//51] += 1
print(qs[0]*qs[1]*qs[2]*qs[3])
