import sys,re
p,s=[l for l in sys.stdin],0
x=len(p)
f=lambda l:[''.join([l[i][d-i-1]for i in range(max(0,d-x),min(d,x))])for d in range(1,x*2)]
for l in p+f(p)+f(p[::-1])+list(map(''.join,zip(*p))):s+=len(re.findall(r'XMAS',l+l[::-1]))
print(s)
