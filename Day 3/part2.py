file = open('input.txt', 'r')

total_priority = 0

bags=file.read().split('\n')
print(bags)

groupedBags = [bags[i:i+3] for i in range(0, len(bags), 3)]

for b1, b2, b3 in groupedBags:
    commonLetters = list(set(b1) & set(b2) & set(b3))
    itemVal = commonLetters[0]

    if itemVal.isupper():
        priorityVal = ord(itemVal)
        priorityVal -= 38
        total_priority += priorityVal

    else: 
        priorityVal = ord(itemVal)
        priorityVal -= 96
        total_priority += priorityVal
    print(itemVal, priorityVal)

print(total_priority)