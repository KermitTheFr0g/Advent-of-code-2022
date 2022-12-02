file = open('input.txt', 'r')

win = {
    "A": "B",
    "B": "C",
    "C": "A"
}

loss = {
    "A": "C",
    "B": "A",
    "C": "B"
}

scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

total_score = 0

for i in file:
    hand_score = 0
    round_score = 0

    hands = i.split(' ')
    hands[1] = hands[1].strip('\n')
    
    if hands[1] == "X":
        toPlay = loss[hands[0]]
        round_score = 0
        hand_score = scores[toPlay]
    elif hands[1] == "Y":
        toPlay = hands[0]
        round_score = 3
        hand_score = scores[toPlay]
    elif hands[1] == "Z":
        toPlay = win[hands[0]]
        round_score = 6
        hand_score = scores[toPlay]

    total_score += (round_score + hand_score)

print(f'Total score: {total_score}')
