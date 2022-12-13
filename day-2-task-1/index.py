with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip().lower() for entry in lines]

points = 0
choiceMapping = {
    "a": "rock",
    "b": "paper",
    "c": "scissors",
    "x": "rock",
    "y": "paper",
    "z": "scissors",
}

scoreMapping = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def getScore(opponentChoice, ourChoice) -> int:
    app = choiceMapping[opponentChoice]
    our = choiceMapping[ourChoice]
    baseScore = scoreMapping[our]

    if app == our:
        print(f"{app} {our} - draw")
        return baseScore + 3

    elif our == "rock":
        if app == "scissors":
            print(f"{app} {our} - win")
            return baseScore + 6
        if app == "paper":
            print(f"{app} {our} - loss")
            return baseScore

    elif our == "paper":
        if app == "rock":
            print(f"{app} {our} - win")
            return baseScore + 6
        if app == "scissors":
            print(f"{app} {our} - loss")
            return baseScore

    elif our == "scissors":
        if app == "paper":
            print(f"{app} {our} - win")
            return baseScore + 6
        if app == "rock":
            print(f"{app} {our} - loss")
            return baseScore

for input in lines:
    inputs = input.split(" ")
    curr_score = getScore(input[0], inputs[1])
    print(curr_score)
    points += curr_score

print(points)