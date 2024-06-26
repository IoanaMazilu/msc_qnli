balls_types_premise = 3
balls_types_hypothesis = 4
board_games_types_premise = 6
board_games_types_hypothesis = 6

# the hypothesis refers to the number of types of balls and board games in the toy store
if balls_types_premise >= balls_types_hypothesis:
    # check if the number of types of balls in the premise contradicts the hypothesis
    label = "contradiction"
elif board_games_types_premise!= board_games_types_hypothesis:
    # check if the number of types of board games in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
