import re


def close_int(n):
    return n-n//1 < 1e-3


s = 0
for machine in open(0).read().split('\n\n'):
    m = list(map(int, re.findall(r'\d+', machine)))
    # ba, bb, prize = matches[:2], matches[2:4], matches[4:6]
    a = round((m[4]*m[3]-m[5]*m[2])/(m[0]*m[3] - m[1]*m[2]))
    b = round((m[4]-m[0]*a)/m[2])
    possible = m[0]*a+m[2]*b == m[4] and m[1]*a+m[3]*b == m[5]
    if possible:
        s += a*3+b
print(s)
