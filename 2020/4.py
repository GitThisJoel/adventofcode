import sys
tags=[byr,iyr,eyr,hgt,hcl,ecl,pid]
def checkpass(pp):
    kv={}
    #print(pp)
    fields=set()
    for l in pp:
        ids=l.split()
        for id in ids:
            #print(id)
            fields.add(id.split(':')[0])
    if 'cid' in fields:
        fields.remove('cid')
    if len(fields)==7:
        info=' '.join(pp)
        for i in info:
            k=i.split(':')
            if k[1][-2:]='\n':
                k[1]=k[1][-2:]
            kv[k[0]]=kv[1]
        ok=False
        for t in tags: #tags=[byr,iyr,eyr,hgt,hcl,ecl,pid]
            v=kv[t]
            switch(t){
                case 'byr': ... 
                break;
                case 'iyr':
                case 'eyr':
                case 'hgt':
                case 'hcl':
                case 'ecl':
                case 'pid':
            }
        return ok
    else:
        return False
passport=[]
valid=0
for line in sys.stdin:
    if line=='\n':
        if checkpass(passport):
            valid+=1
        passport=[]
    else:
        passport.append(line)
if checkpass(passport):
    valid+=1
print(valid)
