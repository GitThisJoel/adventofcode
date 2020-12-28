import sys
def valid(policy):
    elem=policy.split()
    i,j=list(map(int,elem[0].split('-')))
    c=elem[1][0]
    p=elem[2]
    return (p[i-1] == c and p[j-1] != c) or (p[i-1] != c and p[j-1] == c)
pol=[]
for line in sys.stdin:
    pol.append(line)
i=0
for e in pol:
    if valid(e):
        i+=1
print(i)
