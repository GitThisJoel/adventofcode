nav=open('input','r').read().split()
# dir=[[1,0],[0,1],[-1,0],[0,-1]]
pos=[0,0]
d=[1,0]
wp=[10,1]
for n in nav:
    i=n[0]
    v=int(n[1:])
    if i=='N':
        wp[1]+=v
    elif i=='S':
        wp[1]-=v
    elif i=='E':
        wp[0]+=v
    elif i=='W':
        wp[0]-=v
    elif i=='L':
        t=int(v/90)
        if t==1:
            wp=[-wp[1],wp[0]]
        elif t==2:
            wp=[-wp[0],-wp[1]]
        elif t==3:
            wp=[wp[1],-wp[0]]
    elif i=='R':
        t=int(v/90)
        if t==1:
            wp=[wp[1],-wp[0]]

        elif t==2:
            wp=[-wp[0],-wp[1]]
        elif t==3:
            wp=[-wp[1],wp[0]]
    elif i=='F':
        pos=[pos[0]+v*wp[0],pos[1]+v*wp[1]]
print(pos)
print(abs(pos[0])+abs(pos[1]))
