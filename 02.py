# --- Day 2: Rock Paper Scissors ---

# Input
with open('Inputs/input02.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


# Dicts for shape and outcome scores
opponent_shape_scores = {"A": 1,
                         "B": 2,
                         "C": 3}

my_shape_scores = {"X": 1,
                   "Y": 2,
                   "Z": 3}

outcome_scores = {"win": 6,
                  "draw": 3,
                  "loss": 0}

combinations_outcome_dict = {
                     "A X": "draw",
                     "A Y": "win",
                     "A Z": "loss",

                     "B X": "loss",
                     "B Y": "draw",
                     "B Z": "win",

                     "C X": "win",
                     "C Y": "loss",
                     "C Z": "draw",
                     }


def calculate_score(strategy, my_shape_dict, combinations_dict, outcome_dict):
    # Read through lines, calculate total shape score (me) + outcome score
    running_score = 0
    for line in strategy:
        # Shape score
        running_score += my_shape_dict[line[2]]
        # Outcome score
        running_score += outcome_dict[combinations_dict[line]]

    return running_score


print(calculate_score(lines, my_shape_scores, combinations_outcome_dict, outcome_scores))


# Part Two
outcome_decode_dict = {"X": "loss",
                       "Y": "draw",
                       "Z": "win"}

combinations_shape_dict = {
                     "A X": "C",
                     "A Y": "A",
                     "A Z": "B",

                     "B X": "A",
                     "B Y": "B",
                     "B Z": "C",

                     "C X": "B",
                     "C Y": "C",
                     "C Z": "A",
                     }


def calculate_score_properly(strategy, opp_shape_dict, outcome_matching_dict, required_shape_dict, outcome_dict):
    # Read through lines, calculate total shape score (me) + outcome score
    running_score = 0
    for line in strategy:
        # Outcome score
        running_score += outcome_dict[outcome_matching_dict[line[2]]]
        # Shape score
        running_score += opp_shape_dict[required_shape_dict[line]]

    return running_score


print(calculate_score_properly(lines, opponent_shape_scores, outcome_decode_dict, combinations_shape_dict,
                               outcome_scores))
