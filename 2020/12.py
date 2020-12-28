nav=open('input','r').read().split()
dir=[[1,0],[0,1],[-1,0],[0,-1]]
pos=[0,0]
d=[1,0]
deg=0
for n in nav:
    i=n[0]
    v=int(n[1:])
    if i=='N':
        pos[1]+=v
    elif i=='S':
        pos[1]-=v
    elif i=='E':
        pos[0]+=v
    elif i=='W':
        pos[0]-=v
    elif i=='L':
        t=int(v/90)
        deg=(deg+t)%4
        d=dir[deg]
    elif i=='R':
        t=int(v/90)
        deg=(deg-t)%4
        d=dir[deg]
    elif i=='F':
        pos=[pos[0]+d[0]*v,pos[1]+d[1]*v]
print(abs(pos[0])+abs(pos[1]))
