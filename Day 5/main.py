file = open('input.txt', 'r')

stacks = {
    1: ["R", "G", "J", "B", "T", "V", "Z"],
    2: ["J", 'R', 'V', 'L'],
    3: ['S', 'Q', 'F'],
    4: ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
    5: ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
    6: ['S', 'W', 'T', 'C', 'H', 'F'],
    7: ['D', 'Z', 'C', 'V', ],
    8: [],  
    9: []
}

for i in file:
    line = i.split(' ')
