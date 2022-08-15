import sys
def count(lines, pos):
    c = 0
    for l in lines:
        if l[pos] == '1':
            c += 1
    return c, len(lines)

lines = []
one_count = 0
for line in sys.stdin:
    lines.append(line.strip())
lines_cpy = lines.copy()
exit = False
ind = 0
oxygen = ""

# oxygen
while not exit:
    one_count, nol = count(lines, ind)
    most_common = '1' if one_count >= nol/2 else '0'
    dels = []
    for i in range(len(lines)):
        line = lines[i]
        if line[ind] != most_common:
            dels.append(i)

    for d in dels[::-1]:
        del lines[d]
        if len(lines) == 1:
            exit = True
            oxygen = lines[0]
            break
    ind += 1
print(oxygen)


exit = False
ind = 0
co2 = ""
lines = lines_cpy
# co2
while not exit:
    one_count, nol = count(lines, ind)
    most_common = '1' if one_count < nol/2 else '0'
    dels = []
    for i in range(len(lines)):
        line = lines[i]
        if line[ind] != most_common:
            dels.append(i)

    for d in dels[::-1]:
        del lines[d]
        if len(lines) == 1:
            exit = True
            co2 = lines[0]
            break
    ind += 1

print(co2)
print("output =", int(oxygen,2)*int(co2,2))
