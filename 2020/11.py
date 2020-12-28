ls=open('input','r').read().split()
maxx=len(ls[0])
maxy=len(ls)
# gives a list of neigbouring nodes in prevls
def adjacent(x,y):
    adj=[]
    # corners
    if (x,y)==(0,0):
        adj.append(prevls[1][0])
        adj.append(prevls[0][1])
        adj.append(prevls[1][1])
    elif (x,y)==(maxx-1,0):
        adj.append(prevls[maxx-1][1])
        adj.append(prevls[maxx-2][0])
        adj.append(prevls[maxx-2][1])
    elif (x,y)==(0,maxy-1):
        adj.append(prevls[1][maxy-1])
        adj.append(prevls[0][maxy-2])
        adj.append(prevls[1][maxy-2])
    elif (x,y)==(maxx-1,maxy-1):
        adj.append(prevls[maxx-2][maxy-1])
        adj.append(prevls[maxx-1][maxy-2])
        adj.append(prevls[maxx-2][maxy-2])
    # edges
    elif x==0:
        adj.append(prevls[y-1][x:x+2])
        adj.append(prevls[y][x+1])
        adj.append(prevls[y+1][x:x+2])
    elif x==maxx-1:
        adj.append(prevls[y-1][x-1:x+1])
        adj.append(prevls[y][x-1])
        adj.append(prevls[y+1][x-1:x+1])
    elif y==0:
        adj.append(prevls[y][x-1])
        adj.append(prevls[y][x+1])
        adj.append(prevls[y+1][x-1:x+2])
    elif y==maxy-1:
        adj.append(prevls[y][x-1])
        adj.append(prevls[y][x+1])
        adj.append(prevls[y-1][x-1:x+2])
    # all else
    else:
        adj.append(prevls[y-1][x-1:x+2])
        adj.append(prevls[y][x-1])
        adj.append(prevls[y][x+1])
        adj.append(prevls[y+1][x-1:x+2])
    return ''.join(adj)
prevls=[]
newls=ls.copy()
while not prevls==newls:
    prevls=newls.copy()
    for i in range(maxy):
        for j in range(maxx):
            c=prevls[i][j]
            if c=='L':
                if adjacent(j,i).count('#')==0:
                    s=newls[i][0:j]+'#'+newls[i][j+1:maxx]
                    newls[i]=s
            elif c=='#':
                if adjacent(j,i).count('#')>=4:
                    s=newls[i][0:j]+'L'+newls[i][j+1:maxx]
                    newls[i]=s
#print('\n'.join(newls))
sum=0
for l in newls:
    sum+=l.count('#')
print(sum)
