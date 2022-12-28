# --- Day 6: Tuning Trouble ---

# Input
with open('Inputs/input06.txt') as f:
    lines = f.readlines()
    # lines = [line.replace('\n', '') for line in lines]


# Part One


def find_marker_location(signal):
    # Need to find first instance of four different consecutive characters
    for iterable in range(len(signal)-3):
        signal_set = set([x for x in signal[iterable:iterable+4]])
        if len(signal_set) == 4:
            print(signal_set)
            return iterable + 3 + 1  # +1 Because want to account for string being zero-indexed


print(find_marker_location(lines[0]))


# Part Two

def find_message_location(signal):
    # Need to find first instance of four different consecutive characters
    for iterable in range(len(signal)-13):
        signal_set = set([x for x in signal[iterable:iterable+14]])
        if len(signal_set) == 14:
            print(signal_set)
            return iterable + 13 + 1  # +1 Because want to account for string being zero-indexed


print(find_message_location(lines[0]))
