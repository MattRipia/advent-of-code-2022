from dataclasses import dataclass
import numpy as np

@dataclass
class pair:
    firstRangeStr: str
    secondRangeStr: str
    firstRangeInt: list
    secondRangeInt: list


    def __init__(self, firstRangeStr, secondRangeStr):
        self.firstRangeStr = firstRangeStr
        self.secondRangeStr = secondRangeStr

        # list comprehension
        self.firstRangeInt = [int(i) for i in self.firstRangeStr.split("-")]
        self.secondRangeInt = [int(i) for i in self.secondRangeStr.split("-")]

#2-4,6-8
#2-3,4-5
#5-7,7-9
#2-8,3-7
#6-6,4-6
#2-6,4-8

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

pairs = []
for line in lines:
    firstPair, secondPair = line.split(",")
    pairs.append(pair(firstPair, secondPair))

count = 0
for pair in pairs:
    print(pair)
    _first_range = {i for i in range(pair.firstRangeInt[0], pair.firstRangeInt[1] + 1)}
    _second_range = {i for i in range(pair.secondRangeInt[0], pair.secondRangeInt[1] + 1)}
    print(_first_range)
    print(_second_range)
    if _first_range.issubset(_second_range):
        print("FIRST RANGE INSIDE SECOND RANGE")
        count+=1
    elif _second_range.issubset(_first_range):
        print("SECOND RANGE INSIDE FIRST RANGE")
        count+=1
print(count)

        
        

        
        
