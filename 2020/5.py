import sys
row73=[]
def seat(bp):
    row=0
    col=0
    s=''
    for i in range(7):
        c=bp[i]
        if c == 'B':
            s+='1'
        else:
            s+='0'
    row=int(s,2)
    s=''
    for i in range(7,10):
        c=bp[i]
        if c=='R':
            s+='1'
        else:
            s+='0'
        col=int(s,2)
    if row == 73:
        row73.append([row,col])
    return(row*8+col)
max=-1
tot=0
for line in sys.stdin:
    tot+=1
    t=seat(line[:-1])
    if t > max:
        max=t
print(max)
print(tot)
print(row73)
print(73*8+3)
