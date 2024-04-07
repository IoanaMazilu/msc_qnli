# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections W of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with less than 3 types of balls and 6 types of board games, how many different selections W of the 4 items can Amanda make?
# Golden Label: contradiction

ball_types_premise = 3
ball_types_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of ball types and board games mentioned in the premise
if ball_types_hypothesis >= ball_types_premise:
    # check if the hypothesis estimate contradicts the number of ball types in the premise
    label = "contradiction"
elif board_games_hypothesis != board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

