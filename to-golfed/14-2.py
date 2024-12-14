import re

pos, vel = [], []
for line in open(0).readlines():
    pos += [list(map(int, re.findall(r'p=(\d+),(\d+)', line)[0]))]
    vel += [list(map(int, re.findall(r'v=(-?\d+),(-?\d+)', line)[0]))]


def mean_all(poses):
    s = [0, 0]
    for p in poses:
        s = [s[0]+p[0], s[1]+p[1]]
    return [s[0]/len(poses), s[1]/len(poses)]


def variance(poses):
    mean = mean_all(poses)
    s = [0, 0]
    for p in poses:
        s = [s[0]+(mean[0]-p[0])**2, s[1]+(mean[1]-p[1])**2]
    return [s[0]/len(poses), s[1]/len(poses)]


sec = 0
var = variance(pos)
score = var[0]+var[1]
run_mean = score
while True:
    var = variance(pos)
    score = var[0]+var[1]
    if (abs(score-run_mean)/run_mean > 0.4):
        print(sec)
        break
        # print(sec, run_mean, score, abs(score-run_mean)/run_mean*100//1)
        # for y in range(103):
        #     for x in range(101):
        #         print(pos.count([y, x]) or '.', end='')
        #     print()
    run_mean = run_mean*0.8+score*0.2

    for i in range(len(pos)):
        v = vel[i]
        pos[i] = [(pos[i][0]+v[0]) % 101, (pos[i][1] + v[1]) % 103]

    sec += 1
