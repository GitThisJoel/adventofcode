import sys
nol = 0
one_count = [0] * 12
for line in sys.stdin:
    nol += 1
    for i in range(len(line)):
        if line[i] == '1':
            one_count[i] += 1
gamma = ""
epsilon = ""
for v in one_count:
    if v > nol//2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(gamma,2)*int(epsilon,2))
