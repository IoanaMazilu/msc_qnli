balls_premise = 3
balls_hypothesis = 1
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of balls and board games in the toy store, which are also mentioned in the premise
if balls_hypothesis!= balls_premise:
    # check if the number of balls in the hypothesis contradicts the number of balls reported in the premise
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
