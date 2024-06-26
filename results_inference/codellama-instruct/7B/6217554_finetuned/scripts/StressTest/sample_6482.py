balls_store_premise = 3
balls_store_hypothesis = 1
board_games_store_premise = 6
board_games_store_hypothesis = 6

# the hypothesis talks about the number of different types of balls and board games in the toy store
# any number of different types of balls and board games in the store contradicts the premise
if balls_store_hypothesis!= balls_store_premise or board_games_store_hypothesis!= board_games_store_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
