with open('input.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

elf_sums = []
curr_sum = 0
for entry in calories:
    if entry != '':
        curr_sum += int(entry)
    elif entry == '':
        elf_sums.append(curr_sum)
        curr_sum = 0

print(f"The most calories is {max(elf_sums)}")