import re,functools
r,p=map(lambda l:[re.split(r',|\|',s)for s in l.split('\n')],open(0).read()[:-1].split('\n\n'))
print(sum(map(lambda l:(l not in p)*int(l[len(l)//2]),map(lambda l:sorted(l,key=functools.cmp_to_key(lambda a,b:([b,a]in r)-1)),p))))
