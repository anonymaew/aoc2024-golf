from time import sleep
w=131
table = open(0).read()
trail = "^>v<"
di,guarddir,pos = 0,[-w,1,w,-1],table.index('^')

def isloop(o):
    edge,c=".#"[o%w<w-1],0
    if o%w==0:
        print(o//w)
    d,p,t=di,pos,table[:o]+edge+table[o+1:]
    while (0<=p%w<w-1 and 0<=p//w<w-1):
        nextpos=p+guarddir[d]
        if not 0<=nextpos<130*131 or nextpos%w==w-1:
            return False
        if t[nextpos]!="#":
            t=t[:p]+trail[d]+t[p+1:]
            c+=1
            p=nextpos
        else:
            d=(d+1)%4
        if c > 3**9:
            print('timeout', o)
            return True
    return False

print(sum(map(isloop,range(3**9))))
