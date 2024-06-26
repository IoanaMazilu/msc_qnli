ball_premise = 6
ball_hypothesis = 1

board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of ball and board games mentioned in the premise
if ball_premise <= ball_hypothesis and board_games_premise == board_games_hypothesis:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
else:
    # if the hypothesis values contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)
