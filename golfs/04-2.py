import sys,re
p=[l for l in sys.stdin]
e,s,x=enumerate,0,len(p)
for i,l in e(p[1:-1]):
  for j,c in e(l[1:-1]):
    if c=='A':
      u,d=p[i][j]+p[i+2][j+2],p[i][j+2]+p[i+2][j]
      s+=(u=='SM'or u=='MS')and(d=='SM'or d=='MS')
print(s)
