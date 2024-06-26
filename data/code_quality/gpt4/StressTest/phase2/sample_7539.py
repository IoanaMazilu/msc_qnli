ball_premise = 1
ball_hypothesis = 6
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda bought, which is also mentioned in the premise
if ball_premise > ball_hypothesis:
    # check if the number of balls in the premise contradicts the hypothesis
    label = "contradiction"
elif board_games_premise != board_games_hypothesis:
    # check if the number of board games in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
