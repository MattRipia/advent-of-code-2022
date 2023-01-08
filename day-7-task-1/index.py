def parseLine(line: str):
    if line.__contains__("cd"):
        moveTo = line.split(" ")[-1]
        print(line)
        print(moveTo)


with open('input_test.txt', 'r') as infile:
    lines = [line.strip() for line in infile]

for line in lines:
    parseLine(line)
