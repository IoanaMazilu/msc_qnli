balls_premise = 7
balls_hypothesis = 1
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of balls and board games bought by Amanda mentioned in the premise
if balls_hypothesis >= balls_premise:
    # check if the number of 'balls_hypothesis' contradicts the number of balls in the premise
    label = "contradiction"
elif board_games_hypothesis != board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
elif balls_hypothesis < balls_premise and board_games_hypothesis == board_games_premise:
    # the number of balls and board games in the hypothesis are consistent with the premise, thus we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
