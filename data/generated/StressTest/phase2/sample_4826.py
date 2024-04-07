# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections Q of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with 5 types of balls and 6 types of board games, how many different selections Q of the 4 items can Amanda make?
# Golden Label: contradiction

ball_types_premise = 3
ball_types_hypothesis = 5
board_games_types_premise = 6
board_games_types_hypothesis = 6

# the hypothesis refers to the types of balls and board games mentioned in the premise
if ball_types_premise != ball_types_hypothesis:
    # check if the number of ball types in the hypothesis contradicts the number of ball types in the premise
    label = "contradiction"
elif board_games_types_premise != board_games_types_hypothesis:
    # check if the number of board game types in the hypothesis contradicts the number of board game types in the premise
    label = "contradiction"
else:
    # if there are no contradictions, the relation is neutral as the premise does not provide explicit information about the different selections Q
    label = "neutral"

print(label)

