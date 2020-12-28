import sys
ground=[]
for line in sys.stdin:
    ground.append(line)
xlen=len(ground[0])
ylen=len(ground)
steps = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees=[0]*5
for i in range(5):
    xstep=steps[i][0]
    ystep=steps[i][1]
    x=0
    # y=0 not needed
    for y in range(0,ylen,ystep):
        # print(x,y,ground[y][x])
        if ground[y][x] == '#':
            trees[i]+=1
        x=(x+xstep)%(xlen-1) # have a char in the end for some reason 
mult=1
for x in trees:
    mult*=x
print(trees)
print(mult)
