nums=list(map(int,open('input','r').read().split('\n')[:-1]))
prelude=25
def possible(xs,e): # prelude and expected value
    s=set(xs)
    for x in xs:
        if ((e-x) in s) and not ((e-2*x)==0): # is there only one x?
            return True
    return False
for i in range(prelude,len(nums)):
    if not possible(nums[i-prelude:i],nums[i]):
        print(nums[i])
        break
