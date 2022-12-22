import re

def move_containers(instruction: str, stack_dict: dict):

    stripped = str(instruction.strip())
    _frag_instructions = re.findall(r'\d+', stripped)

    moves = int(_frag_instructions[0])
    from_stack = int(_frag_instructions[1])
    to_stack = int(_frag_instructions[2])

    print("Moves:", moves)
    print("From:", from_stack)
    print("To:", to_stack)

    print("Before Move:")
    for key in stack_dict.keys():
        print(key, stack_dict[key])

    # Determine slice index
    slice_index = len(stack_dict[from_stack]) - moves
    print("Slice Index:", slice_index)

    # add n items from the 'from' stack and add them to the 'to' stack
    stack_dict[to_stack].extend(stack_dict[from_stack][slice_index:])

    # removes n items from the 'from' stack
    stack_dict[from_stack] = stack_dict[from_stack][:slice_index]


    print("After Move:")
    for key in stack_dict.keys():
        print(key, stack_dict[key])

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

with open('input.txt', 'r') as infile:
    lines = [line for line in infile]

# read input into 3 lists depending on the new line
line_no = 0
for line in lines:
    if line == "\n":
        stacks = lines[:line_no - 1]
        instructions = lines[line_no + 1:]
        num_stacks = lines[line_no - 1]
    line_no += 1

# find the number of stacks from input (1   2   3) -> get last index convert to int
num_stacks = int(num_stacks.strip().split("   ")[-1])

# create stacks
stack_dict = {}
for count in range(1, num_stacks + 1):
    stack_dict[count] = list()
# print(stack_dict)

# Divide up each line from 'stacks' and find the stack to dump the character
for line in stacks:
    count = 0
    for char in line:
        bucket_no = int(count / 4) + 1
        if char.isalpha():
            stack_dict[bucket_no].append(char)
        count+=1

# reverse to get the correct stack
for key in stack_dict.keys():
    stack_dict[key].reverse()
    print(key, stack_dict[key])

# perform the stack swapping
for instruction in instructions:
    move_containers(instruction, stack_dict)

chars = ''
for key in stack_dict.keys():
    char = stack_dict[key][-1]
    chars += char

print(chars)