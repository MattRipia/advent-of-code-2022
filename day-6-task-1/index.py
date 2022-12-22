
with open('input.txt', 'r') as infile:
    lines = [line for line in infile]

line = lines[0]

char_array = []
char_array.extend(line)
print(char_array)

num_chars = len(char_array)
print(num_chars)

marker_no = 4
char_dict = {}

for i in range(0 , num_chars):
    unique = False
    remainder = int(i % marker_no)
    print(i, " - ", remainder, " - ", char_array[i])
    char_dict[remainder] = char_array[i]
    curr_set = {x for x in char_dict.values() if x}
    print(curr_set)
    if len(curr_set) > marker_no - 1:
        print("EXITING: ", i+1)
        exit(0)
    