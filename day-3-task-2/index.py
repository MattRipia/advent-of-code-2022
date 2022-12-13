from dataclasses import dataclass
import numpy as np

@dataclass
class Rucksack:
    rucksackSize: int
    compartmentSize: int
    rucksackContents: str
    firstCompartment: str
    secondCompartment: str

    valid: bool = False

    def __init__(self, rucksackSize: int, rucksackContents: str):
        self.rucksackContents = rucksackContents
        self.rucksackSize = rucksackSize
        self.compartmentSize = int(self.rucksackSize / 2)
        self.firstCompartment = rucksackContents[0:self.compartmentSize]
        self.secondCompartment = rucksackContents[self.compartmentSize:rucksackSize]
        self.valid = True if (len(self.firstCompartment) == self.compartmentSize and len(self.secondCompartment) == self.compartmentSize) else False

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

rucksacks = []

for line in lines:
    totalLineChars = len(line)
    rucksacks.append(Rucksack(totalLineChars, line))

total = 0
numGroups = len(rucksacks) / 3
groups = np.array_split(rucksacks, numGroups)

for group in groups:
    print("A new Group:")
    strArray = []
    for rucksack in group:
        strArray.append(rucksack.rucksackContents)
    print(strArray)

    # A map in python will apply a given function to each item of an iterable (string array)
    # In this case, each string in the string array is turned into a set.
    
    stringSet = map(set, strArray)

    # the array list gets trasformed into the following:
    # ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
    # index 0: {'r', 'p', 'v', 'F', 'h', 'J', 'M', 'W', 's', 'f', 'w', 't', 'c', 'g'}
    # index 1: {'r', 'R', 'D', 'F', 'q', 'Z', 'M', 'S', 'G', 's', 'f', 'z', 'N', 'H', 'j', 'L'}
    # index 2: {'r', 'B', 'v', 'V', 'P', 'q', 'd', 'W', 'm', 'z', 'w', 'T', 'g'}

    # we can then do an intersection by expanding the set and using set.intersection on it
    # then we pop the common char from the set and return it (there is only 1 value here!)
    commonChar = set.intersection(*stringSet).pop()

    # Get the ascii representation and transform so 'A = 1' and 'a = 27'
    asciiValue = int(ord(commonChar))
    if asciiValue >= 97:
        value = asciiValue - 96
    if asciiValue <= 96:
        value = asciiValue - 38
    print(f"Char: {commonChar}")
    print(f"Value: {value}")
    total += value
print(total)
   
