file = open('input.txt', 'r')

total_priority = 0

for i in file:
    rucksackLen = len(i)
    c1 = i[:rucksackLen // 2]
    c2 = i[rucksackLen // 2:]

    commonItem = list(set(c1)& set(c2))
    itemVal = commonItem[0]

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