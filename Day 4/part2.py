file = open('input.in', 'r')

lines = file.read().strip().split()

total_overlaps = 0

for line in lines:
    elves = line.split(',')
    ranges = [list(map(int, elf.split('-'))) for elf in elves]

    a, b = ranges[0]
    c, d = ranges[1]

    if not(b < c or d < a):
        total_overlaps += 1

print(total_overlaps)