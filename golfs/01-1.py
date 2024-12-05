l,s=open(0).read().split(),sorted
print(sum([abs(int(p)-int(q))for p,q in zip(*[s(l[::2]),s(l[1::2])])]))
