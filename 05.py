# --- Day 5: Supply Stacks ---

# Input
with open('Inputs/input05.txt') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]


class Crates:
    def __init__(self, full_input):
        self.full_input = full_input
        # Get the number of stacks
        self.num_stacks = int((len(full_input[0])+1) / 4)

        # Get instructions and drawing separated
        self.drawing = full_input[:8]
        self.instructions = full_input[10:]
        self.levels = len(self.drawing)

    def get_stack_dict(self):
        stack_dict = {}

        for stack in range(self.num_stacks):
            stack_dict[stack+1] = ''
            for level in range(self.levels):
                stack_dict[stack+1] += self.drawing[level][stack*4+1].strip()  # Strip ensures "blanks" aren't added
        return stack_dict

    def process_instruction_9000(self, stack_dict, instruction):
        num_crates = int(instruction.split(' ')[1])
        origin = int(instruction.split(' ')[3])
        target = int(instruction.split(' ')[-1])

        # Reverse crate order from origin
        reversed_crates = stack_dict[origin][:num_crates][::-1]

        # Remove crates from stack dict
        stack_dict[origin] = stack_dict[origin][num_crates:]

        # Add crates to target
        stack_dict[target] = reversed_crates + stack_dict[target]

        return stack_dict

    def process_instruction_9001(self, stack_dict, instruction):
        num_crates = int(instruction.split(' ')[1])
        origin = int(instruction.split(' ')[3])
        target = int(instruction.split(' ')[-1])

        # Don't reverse crate order from origin!
        moved_crates = stack_dict[origin][:num_crates]

        # Remove crates from stack dict
        stack_dict[origin] = stack_dict[origin][num_crates:]

        # Add crates to target
        stack_dict[target] = moved_crates + stack_dict[target]

        return stack_dict

    def parse_instructions_9000(self):
        stack_dict = self.get_stack_dict()

        for instruction in self.instructions:
            stack_dict = self.process_instruction_9000(stack_dict, instruction)
        return stack_dict

    def parse_instructions_9001(self):
        stack_dict = self.get_stack_dict()

        for instruction in self.instructions:
            stack_dict = self.process_instruction_9001(stack_dict, instruction)
        return stack_dict


arrangement = Crates(lines)
stacks = arrangement.parse_instructions_9000()

# Get top crates
top_crates = ''
for stack in range(len(stacks)):
    top_crates += stacks[stack+1][0]

print(top_crates)


# Part Two: Modified class above to deal with changes
arrangement = Crates(lines)
stacks = arrangement.parse_instructions_9001()

# Get top crates
top_crates = ''
for stack in range(len(stacks)):
    top_crates += stacks[stack+1][0]

print(top_crates)


