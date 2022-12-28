# --- Day 7: No Space Left On Device ---

with open('Inputs/input07.txt') as f:
    lines = f.readlines()
    # lines = [line.replace('\n', '') for line in lines]


# Part One


def calc_directory_sizes(command_line_output):
    # Iterate through lines, keeping track of what directories we are in
    directories_size_dict = {}
    current_directories = []
    for line in command_line_output:
        if line.startswith("$ cd .."):
            current_directories.pop()
        elif line.startswith("$ cd"):
            # NOTE: This didn't originally account for the fact that folders in DIFFERENT directories could share names!
            current_directories.append(line.split()[2])
            directories_size_dict["/".join(current_directories)] = 0
        elif line.split()[0].isnumeric():
            # Add size to all directories/ subdirectories we are currently in
            for ID, _ in enumerate(current_directories):
                directories_size_dict["/".join(current_directories[:ID+1])] += int(line.split()[0])

    return directories_size_dict


direc_sizes_dict = calc_directory_sizes(lines)
print(sum([x for x in direc_sizes_dict.values() if x <= 100000]))


# Part Two


current_free_space = direc_sizes_dict["/"]
size_of_direc_to_delete = min([x for x in direc_sizes_dict.values() if x >= 30000000 - (70000000 - current_free_space)])
print(size_of_direc_to_delete)

# Cleaner solution: https://tinyurl.com/ytzdasz8
