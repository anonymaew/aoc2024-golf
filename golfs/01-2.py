import sys
s=0
p,q=zip(*[map(int,l.split())for l in sys.stdin])
for m in p:
  for n in q:s+=[0,m][m==n]
print(s)
