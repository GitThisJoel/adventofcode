nums=list(map(int,open('input','r').read().split()))
nums.sort()
ds=[0]*4
ds[3]=1 # the last one is always +3
ds[nums[0]]+=1
for i in range(len(nums)-1):
    ds[nums[i+1]-nums[i]]+=1
print(ds[1]*ds[3])
