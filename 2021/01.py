import sys
p = int(input())
count = 0
for line in sys.stdin:
    c = int(line)
    if p < c:
        count += 1
    p = c
print(count)
