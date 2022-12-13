with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip().lower() for entry in lines]

points = 0
choiceMapping = {
    "a": "rock",
    "b": "paper",
    "c": "scissors"
}

strategyMapping = {
    "x": "lose",
    "y": "draw",
    "z": "win",
}

choicePointMap = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

conditionalWinMap = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def getScore(opponentChoice, strategyKey) -> int:
    opp = choiceMapping[opponentChoice]
    strategy = strategyMapping[strategyKey]

    if strategy == "lose":
        our = conditionalWinMap[opp]
        return choicePointMap[our]
    elif strategy == "win":
        our = conditionalWinMap[conditionalWinMap[opp]]
        return 6 + choicePointMap[our]
    elif(strategy == "draw"):
        return 3 + choicePointMap[opp]

for input in lines:
    inputs = input.split(" ")
    curr_score = getScore(input[0], inputs[1])
    points += curr_score

print(points)