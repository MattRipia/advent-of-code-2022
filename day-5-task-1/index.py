
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

initial_dict = {}
for count in range(1, 10):
    initial_dict[count] = list()
print(initial_dict)

for line in lines:
    print(line)
    count = 0;
    for char in line:
        print(count,"(",char,")",(int(count / 4) + 1))
        if char.isalpha():
            initial_dict[int(count / 4) + 1].append(char)
        count+=1
        
print(initial_dict)

# reverse to get the correct stack
for key in initial_dict.keys():
    initial_dict[key].reverse()
    print(initial_dict[key])

initial_dict[1].pop()
print(initial_dict[1])

# do the stack operations  
#      
# 1 = 1
# 5 = 2
# 9 = 3