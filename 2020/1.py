import sys
xs = []
for n in sys.stdin:
    xs.append(int(n))
for i in xs:
    for j in xs[1:]:
        if i+j == 2020:
            print(i*j)
            break
