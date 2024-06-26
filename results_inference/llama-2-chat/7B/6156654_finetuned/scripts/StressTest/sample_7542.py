balls_types = 3
board_games_types = 6

# the hypothesis refers to the number of types of balls and board games in the store, which is also mentioned in the premise
if balls_types < 5 and board_games_types < 6:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
