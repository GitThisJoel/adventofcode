fishes = list(map(int, input().strip().split(',')))
days = 18
new = []
for day in range(1,days+1):
    fishes = list(map(lambda x: x-1, fishes))
    fishes += new
    new = []
    # print(f"After day {day}:", ','.join(list(map(str, fishes))))
    for i in range(len(fishes)):
        if fishes[i] == 0:
            new.append(8)
            fishes[i] = 7 # when minus one => 6
print(len(fishes))
