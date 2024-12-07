from time import sleep
w,c=131,set()
table = open(0).read()
di,guarddir,pos = 0,[-w,1,w,-1],table.index('^')
while(0<=pos%w<w-1 and 0<=pos//w<w-1):
    nextpos=pos+guarddir[di]
    if (table[nextpos]=="#"):
        di=(di+1)%4
    else:
        c|={pos}
        pos=nextpos
print(table)
print(len(c))
