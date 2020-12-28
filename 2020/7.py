import sys
kv={}
for line in sys.stdin:
    l=line.strip().split(' bags contain ')
    k=' '.join(l[0].split()[0:2])
    v=[]
    tempv=l[1].split(',')
    for t in tempv:
        v.append(' '.join(t.split()[1:3]))
    kv[k]=v
for k in kv:
    print(k,'\t=> ',kv[k])
