import sys
xs = []
for n in sys.stdin:
    xs.append(int(n))
first = 1; second = 2;
for i in xs:
    for j in xs:#[first:]:
        for k in xs:#[second:]:
            sum = i+j+k
            if i+j+k == 2020:
                print(i*j*k)
                break
        second += 1
    first += 1
