import sys
s=0
for(p,q)in zip(*[sorted(map(int,n)) for n in zip(*[l.split()for l in sys.stdin])]):s+=abs(p-q)
print(s)
