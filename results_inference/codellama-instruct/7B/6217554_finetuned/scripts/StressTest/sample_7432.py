balls_store_premise = 1
board_games_store_premise = 6
balls_store_hypothesis = 3
board_games_store_hypothesis = 6

# the hypothesis talks about the number of different types of balls and board games in the toy store
if balls_store_hypothesis > balls_store_premise or board_games_store_hypothesis > board_games_store_premise:
    # check if the number of different types of balls or board games in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
