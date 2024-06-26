balls_store_premise = 3
board_games_store_premise = 6

# the hypothesis refers to the number of different selections R of the 4 items that Amanda can make
if balls_store_premise <= 1 and board_games_store_premise == 6:
    # check if the hypothesis value contradicts the estimate of more than '1' type of balls
    label = "contradiction"
elif balls_store_premise == 3 and board_games_store_premise == 6:
    # check if the hypothesis value contradicts the estimate of 3 types of balls
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
