file = open('input.txt', 'r')

total_score = 0

solutions = [
    ["C", "X"],
    ["A", "Y"],
    ["B", "Z"]
]

draws = [
    ['A', 'X'],
    ['B', 'Y'],
    ['C', 'Z']
]

for i in file:
    hand_score = 0
    round_score = 0

    hands = i.split(' ')
    hands[1] = hands[1].strip('\n')

    if hands[1] == "X":
        hand_score = 1
    elif hands[1] == "Y":
        hand_score = 2
    elif hands[1] == "Z":
        hand_score = 3

    if hands in solutions:
        round_score = 6
    elif hands in draws:
        round_score = 3
    
    print(f'{hands} {hand_score + round_score}')

    total_score += (hand_score + round_score)

print(f'Total Score: {total_score}')
