with open('input.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

elf_sums = {}
curr_sum = 0
index = 1

for entry in calories:
    if entry != '':
        curr_sum += int(entry)
    elif entry == '':
        elf_sums[index] = curr_sum
        curr_sum = 0
        index += 1

print(f"The most calories is {max(elf_sums.values())}")

calorie_list = [i for i in elf_sums.values()]
calorie_list.sort()
top_three_calories = calorie_list[-1] + calorie_list[-2] + calorie_list[-3]
print(top_three_calories)
