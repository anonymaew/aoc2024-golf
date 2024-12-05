f=open(0).read().split()
print(sum([(i==j)*int(j)for j in f[1::2]for i in f[::2]]))
