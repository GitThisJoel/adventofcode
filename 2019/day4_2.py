start = 359282
stop = 820401

# 6 digits
# two adjacent number is the same
# left to right never decrese
# more than 2 adjecent is not allowed if not there is a another pair of 2 adjecent
def isOk(x):
    s = str(x)
    occurrence = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            return False

    for i in range(len(s)):
        occurrence[int(s[i])] = occurrence[int(s[i])]+1
    if occurrence.count(2) >= 1:
        return True
    return False

# print("112233 =>", isOk(112233))
# print("123444 =>", isOk(123444))
# print("111122 =>", isOk(111122))
# print("155555 =>", isOk(155555))
# print("111111 =>", isOk(111111))

count = 0
for i in range(start, stop+1):
    if isOk(i):
        count += 1
print(count)
