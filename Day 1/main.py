file = open('input.txt', 'r');

biggestNumber = 0
addition = 0
elves = []

for i in file: 
    if i.strip() == "":
        if addition > biggestNumber:
            biggestNumber = addition
        elves.append(addition)
        addition = 0
    else:
        addition += int(i)

elves.sort()

print(elves);
print(biggestNumber);
print(sum(elves[-3:]))