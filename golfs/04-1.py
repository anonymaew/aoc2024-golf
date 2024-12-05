p,r=open(0).read(),range
print(sum([(l+l[::-1]).count('XMAS')for l in[p]+[p[s::140+i]for s in r(141)for i in r(3)]]))
