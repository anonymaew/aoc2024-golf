p,m=open(0).read(),lambda s:s=="MAS"or s=="SAM"
print(sum([(m(p[i::142][:3])*m(p[i+282::-140][:3]))for i in range(3**9)]))
