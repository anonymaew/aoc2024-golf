import functools as f
@f.cache
def b(n,t):
  if t<1:return 1
  if'0'==n:return b('1',t-1)
  if len(n)%2:return b(str(int(n)*2024),t-1)
  h=len(n)//2;return b(n[:h],t-1)+b(str(int(n[h:])),t-1)
print(sum([b(n,25)for n in open(0).read()[:-1].split(' ')]))
