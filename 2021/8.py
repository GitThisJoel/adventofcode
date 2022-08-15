import sys
def p1():
    n = 0
    lens = {2,3,4,7}
    for line in sys.stdin:
        for w in line.split('|')[1].strip().split():
            if len(w) in lens:
                n += 1
    print(n)

def p2():
    sum = 0;
    for line in sys.stdin:
        signal,digits = line.split('|')
        signal = signal.strip().split()
        digits = digits.strip().split()

        signal.sort(key = lambda x: len(x))
