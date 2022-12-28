# --- Day 4: Camp Cleanup ---

# Input
with open('Inputs/input04.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


# Part One


def find_full_overlaps(assignments):

    # Loop through pairs, find if full overlap exists
    overlap_count = 0
    for assignment_pair in assignments:
        pair1 = assignment_pair.split(',')[0].split('-')
        pair2 = assignment_pair.split(',')[1].split('-')

        # Create sets of numbers
        set1 = set(range(int(pair1[0]), int(pair1[1])+1))
        set2 = set(range(int(pair2[0]), int(pair2[1])+1))

        # If the intersection of the two sets is the same size as the smallest set, then there is a full overlap
        if (len(set1.intersection(set2)) == len(set1)) or (len(set1.intersection(set2)) == len(set2)):
            overlap_count += 1

    return overlap_count


print(find_full_overlaps(lines))


# Part Two


def find_partial_overlaps(assignments):
    # Same as before, but if intersection contains ANY elements, then there is an overlap
    # Loop through pairs, find if full overlap exists
    overlap_count = 0
    for assignment_pair in assignments:
        pair1 = assignment_pair.split(',')[0].split('-')
        pair2 = assignment_pair.split(',')[1].split('-')

        # Create sets of numbers
        set1 = set(range(int(pair1[0]), int(pair1[1]) + 1))
        set2 = set(range(int(pair2[0]), int(pair2[1]) + 1))

        # If the intersection of the two sets is the same size as the smallest set, then there is a full overlap
        if len(set1.intersection(set2)) >= 1:
            overlap_count += 1

    return overlap_count


print(find_partial_overlaps(lines))
