import re
n,e='\n',enumerate
r,p=map(lambda l:[re.split(r',|\|',s)for s in l.split(n)],open(0).read()[:-1].split(n*2))
print(sum(map(lambda l:int(l[len(l)//2]),filter(lambda l:sum([[v,u]in(j>i)*r for j,v in e(l)for i,u in e(l)])==0,p))))
