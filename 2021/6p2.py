inp = list(map(int, input().strip().split(',')))
fishes = [0 for _ in range(9)]
for f in inp:
    fishes[f] += 1
days = 256
for day in range(days):
    n = fishes.pop(0)
    fishes.append(0)
    if n > 0:
        fishes[8] = n
        fishes[6] += n

print(sum(fishes))
