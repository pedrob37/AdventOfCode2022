# --- Day 3: Rucksack Reorganization ---

# Input
with open('Inputs/input03.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


# Part One


def get_shared_items(rucksacks):
    lowercase_items = 'abcdefghijklmnopqrstuvwxyz'
    items = lowercase_items + lowercase_items.upper()

    # Read through each line (rucksack), split in two, and find shared item
    shared_items = []
    shared_items_values = []
    for line in rucksacks:
        line_len = len(line)
        set1 = set(line[:line_len//2])
        set2 = set(line[line_len//2:])
        # Assume only one shared item
        shared_item = list(set1.intersection(set2))[0]
        shared_items.append(shared_item)
        shared_items_values.append(items.index(shared_item)+1)

    return shared_items, shared_items_values


print(sum(get_shared_items(lines)[1]))

# Part Two


def get_badges(rucksack, subgroups_size=3):
    lowercase_items = 'abcdefghijklmnopqrstuvwxyz'
    items = lowercase_items + lowercase_items.upper()

    shared_items = []
    shared_items_values = []
    # Need to aggregate rucksacks in groups of three
    for elf_group in range(len(rucksack)//subgroups_size):
        elf_group_rucksacks = rucksack[elf_group*subgroups_size: (elf_group+1)*subgroups_size]

        # Calculate intersection across all rucksacks in subgroup
        shared_item = list(set(elf_group_rucksacks[0]).intersection(*[set(x) for x in elf_group_rucksacks[1:]]))[0]
        shared_items.append(shared_item)
        shared_items_values.append(items.index(shared_item)+1)

    return shared_items, shared_items_values


print(sum(get_badges(lines, 3)[1]))
