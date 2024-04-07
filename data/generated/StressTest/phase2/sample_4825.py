# Premise: If the toy store is stocked with less than 8 types of balls and 6 types of board games, how many different selections Q of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections Q of the 4 items can Amanda make?
# Golden Label: neutral

types_of_balls_premise = 8
types_of_balls_hypothesis = 3
types_of_board_games_premise = 6
types_of_board_games_hypothesis = 6

# the hypothesis refers to the number of types of balls and board games mentioned in the premise
if types_of_balls_hypothesis >= types_of_balls_premise:
    # check if the number of types of balls in the hypothesis contradicts the premise
    label = "contradiction"
elif types_of_board_games_hypothesis != types_of_board_games_premise:
    # check if the number of types of board games in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

