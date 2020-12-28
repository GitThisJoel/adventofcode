inst=open('input','r').read().split('\n')[:-1]
m=len(inst)
def loop(args):
    vis=set()
    a=0
    exit=False
    prev=[]
    i=0
    while not exit:
        if (i in vis) or (i>=m):
            exit=True
            return [prev,a,(i>=m)]
        else:
            vis.add(i)
            arg=args[i]
            if arg[:3]=='acc':
                a+=int(arg.split()[1])
                i+=1
            elif arg[:3]=='jmp':
                prev.append(i)
                i+=int(arg.split()[1])
            elif arg[:3]=='nop':
                i+=1
            else:
                print(arg,'undefined argument')
    # return [prev,a,False] # should not be reached
js=loop(inst)[0]
te=False
j=0
while not te:
    temp=[]
    temp=inst.copy()
    temp[js[j]]='nop +0'
    ans=loop(temp)
    if ans[2]:
        print(ans[1])
        break
    j+=1
