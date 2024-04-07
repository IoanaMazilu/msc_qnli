# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections W of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with less than 4 types of balls and 6 types of board games, how many different selections W of the 4 items can Amanda make?
# Golden Label: entailment

ball_types_premise = 3
ball_types_hypothesis = 4
board_game_types_premise = 6
board_game_types_hypothesis = 6

# the hypothesis refers to the types of balls and board games mentioned in the premise
if ball_types_premise >= ball_types_hypothesis:
    # check if the 'ball_types_hypothesis' contradicts the number of ball types in the premise
    label = "contradiction"
elif board_game_types_hypothesis != board_game_types_premise:
    # check if the number of board game types in the hypothesis contradicts the number of board game types in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

