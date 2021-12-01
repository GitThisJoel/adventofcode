import sys
m = []
count = 0
for line in sys.stdin:
    m.append(int(line))
p = sum(m[:3])
for i in range(1,len(m)-2):
    c = sum(m[i:i+3])
    if p < c:
        count += 1
    p = c
print(count)
