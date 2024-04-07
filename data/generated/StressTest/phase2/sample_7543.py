# Premise: If the toy store is stocked with less than 5 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Golden Label: neutral

ball_types_premise = 5
ball_types_hypothesis = 3
board_game_types_premise = 6
board_game_types_hypothesis = 6

# the hypothesis refers to the types of balls and board games mentioned in the premise
if ball_types_premise < ball_types_hypothesis:
    # check if the number of ball types in the hypothesis contradicts the premise
    label = "contradiction"
elif board_game_types_premise != board_game_types_hypothesis:
    # check if the number of board game types in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but we cannot infer entailment
    # because the premise gives only an upper limit for the number of ball types
    label = "neutral"

print(label)

