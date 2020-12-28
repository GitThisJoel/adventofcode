nums=list(map(int,open('input','r').read().split()))
nums.sort()
nums=nums+[nums[-1:][0]+3] # added first and last adapters
kv={0:1}
for n in nums:
    kv[n]=0
    if n-1 in kv:
        kv[n]+=kv[n-1]
    if n-2 in kv:
        kv[n]+=kv[n-2]
    if n-3 in kv:
        kv[n]+=kv[n-3]
print(kv[nums[-1:][0]])
