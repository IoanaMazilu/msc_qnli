balls_premise = 3
balls_hypothesis = 1
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of balls and board games in the toy store
if balls_premise <= balls_hypothesis and board_games_premise == board_games_hypothesis:
    # check if the hypothesis values for balls and board games do not contradict the premise values
    label = "entailment"
else:
    # if the hypothesis values for balls or board games contradict the premise values, we have a contradiction
    label = "contradiction"

print(label)
