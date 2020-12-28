file=open('input','r').read().split('\n\n')#[0].split('\n')
sum=0
for l in file:
    l=l.strip()
    kv={}
    p=len(l.split('\n'))
    ans=0
    for cs in l.split('\n'):
        for c in cs:
            if not c in kv:
                kv[c]=0
            kv[c]+=1
    for k in kv:
        if kv[k]==p:
            ans+=1
    sum+=ans
print(sum)
