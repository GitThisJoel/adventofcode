start = 359282
stop = 820401

# 6 digits
# two adjacent number is the same
# left to right never decrese
# more than 2 adjecent is not allowed if not there is a another pair of 2 adjecent
def isOk(x):
    s = str(x)
    adjecent = False
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            return False
        if s[i] == s[i+1]:
            if adjecent or s[i] == s[i-1]:
                adjecent = True
    return adjecent

count = 0
for i in range(start, stop+1):
    if isOk(i):
        count += 1
print(count)
