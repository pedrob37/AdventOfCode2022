# --- Day 1: Calorie Counting ---

# Input
with open('Inputs/input01.txt') as f:
    lines = f.readlines()


# Part One
def find_max_calories(calories_list):
    elf_calorie_count = []
    # Loop through lines, sum values until newline character encountered
    running_count = 0
    for line in calories_list:
        if line != "\n":
            running_count += float(line)
        else:
            elf_calorie_count.append(running_count)
            running_count = 0

    return max(elf_calorie_count), elf_calorie_count


print(find_max_calories(lines)[0])


# Part Two
def find_top_n_calories(calories_list, top_n=3):
    elf_calorie_count = find_max_calories(calories_list)[1]

    # Find top N by iteratively appending, then removing the max value
    top_n_calories = []
    for n in range(top_n):
        current_max = max(elf_calorie_count)
        top_n_calories.append(current_max)
        elf_calorie_count.pop(elf_calorie_count.index(current_max))

    return top_n_calories


print(sum(find_top_n_calories(lines, 3)))
