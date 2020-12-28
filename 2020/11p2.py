ls=open('input','r').read().split()
maxx=len(ls[0])
maxy=len(ls)
def adjacent(x,y):
    dir=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    i=0
    adj=0
    while i<8:
        x1,y1=x,y
        exit=False
        d=dir[i]
        point=''
        x1+=d[0]
        y1+=d[1]
        while (x1>=0 and x1<=maxx-1) and (y1>=0 and y1<=maxy-1) and not exit: #(not (point=='#' or point=='L'))
            #print((x1>=0 and x1<=maxx-1), (y1>=0 and y1<=maxy-1), not exit)
            point=prevls[y1][x1]
            if point=='#':
                adj+=1
                exit=True
            elif point=='L':
                exit=True
            x1+=d[0]
            y1+=d[1]
        i+=1
    return adj
prevls=[]
newls=ls.copy()
while not prevls==newls:
    prevls=newls.copy()
    for i in range(maxy):
        for j in range(maxx):
            c=prevls[i][j]
            if c=='L':
                if adjacent(j,i)==0:
                    s=newls[i][0:j]+'#'+newls[i][j+1:maxx]
                    newls[i]=s
            elif c=='#':
                if adjacent(j,i)>=5:
                    s=newls[i][0:j]+'L'+newls[i][j+1:maxx]
                    newls[i]=s
# print('\n'.join(newls))
# print('------------------------')
sum=0
for l in newls:
    sum+=l.count('#')
print(sum)
