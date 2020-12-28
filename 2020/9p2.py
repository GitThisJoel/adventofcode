nums=list(map(int,open('input','r').read().split('\n')[:-1]))
prelude=25
x=-1
k=-1
def possible(xs,e): # prelude and expected value
    s=set(xs)
    for x in xs:
        if ((e-x) in s) and not ((e-2*x)==0):
            return True
    return False
for i in range(prelude,len(nums)):
    if not possible(nums[i-prelude:i],nums[i]):
        x=nums[i]
        k=i
        break
# bad solution
for i in range(k):
    # print('--------------------------')
    for j in  range(k-1,i,-1):
        # print(nums[i:j],sum(nums[i:j]))
        s=sum(nums[i:j])
        if s==x:
            print(min(nums[i:j])+max(nums[i:j]))
            break
