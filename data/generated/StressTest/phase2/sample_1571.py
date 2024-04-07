# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections E of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with 4 types of balls and 6 types of board games, how many different selections E of the 4 items can Amanda make?
# Golden Label: contradiction

ball_types_premise = 3
ball_types_hypothesis = 4
board_types_premise = 6
board_types_hypothesis = 6

# the hypothesis refers to the type of balls and board games mentioned in the premise
if ball_types_premise != ball_types_hypothesis:
    # check if the number of ball types in the hypothesis contradicts the number of ball types in the premise
    label = "contradiction"
elif board_types_hypothesis != board_types_premise:
    # check if the number of board types in the hypothesis contradicts the number of board types in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

