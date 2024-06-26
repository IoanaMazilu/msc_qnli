balls_types_premise = 3
balls_types_hypothesis = 1
board_games_types_premise = 6
board_games_types_hypothesis = 6

# the hypothesis talks about the number of ball types and board games types in the store
if balls_types_hypothesis!= balls_types_premise:
    # check if the number of ball types in the hypothesis contradicts the number of ball types in the premise
    label = "contradiction"
elif board_games_types_hypothesis!= board_games_types_premise:
    # check if the number of board games types in the hypothesis contradicts the number of board games types in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
