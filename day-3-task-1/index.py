from dataclasses import dataclass

@dataclass
class Rucksack:
    rucksackSize: int
    compartmentSize: int
    firstCompartment: str
    secondCompartment: str
    valid: bool = False

    def __init__(self, rucksackSize: int, rucksackContents: str):
        self.rucksackSize = rucksackSize
        self.compartmentSize = int(self.rucksackSize / 2)
        self.firstCompartment = rucksackContents[0:self.compartmentSize]
        self.secondCompartment = rucksackContents[self.compartmentSize:rucksackSize]
        self.valid = True if (len(self.firstCompartment) == self.compartmentSize and len(self.secondCompartment) == self.compartmentSize) else False
        
def findCommonChar(firstString, secondString):
    for char in firstString:
        for secondChar in secondString:
            if char == secondChar:
                print("FOUND MATCH: ", char)
                return char

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

total = 0

for line in lines:
    totalLineChars = len(line)
    rucksack = Rucksack(totalLineChars, line)
    print(rucksack)
    commonChar = findCommonChar(rucksack.firstCompartment, rucksack.secondCompartment)
    asciiValue = int(ord(commonChar))
    print("prev", asciiValue)
    if asciiValue >= 97:
        value = asciiValue - 96
    if asciiValue <= 96:
        value = asciiValue - 38
    total += value
    print("new ", value)
    print("total", total)

