ball_premise = 1
board_games_premise = 3

# define variables for the hypothesis
ball_hypothesis = -1
board_games_hypothesis = 0

# check if the hypothesis values contradict the premise values
if ball_hypothesis < ball_premise:
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
