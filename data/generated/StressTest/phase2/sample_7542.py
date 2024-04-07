# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with less than 5 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Golden Label: entailment

ball_types_premise = 3
ball_types_hypothesis = 5
board_game_types_premise = 6
board_game_types_hypothesis = 6

# first, compare the number of ball types in the premise and hypothesis
if ball_types_hypothesis <= ball_types_premise:
    # check if the number of ball types in the hypothesis contradicts the number of ball types in the premise
    label = "contradiction"
elif board_game_types_hypothesis != board_game_types_premise:
    # check if the number of board game types in the hypothesis contradicts the number of board game types in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

