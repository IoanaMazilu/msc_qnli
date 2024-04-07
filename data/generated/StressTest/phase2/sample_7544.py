# Premise: If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Hypothesis: If the toy store is stocked with 2 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?
# Golden Label: contradiction

balls_premise = 3
balls_hypothesis = 2
board_games_premise = 6
board_games_hypothesis = 6
items = 4

# the hypothesis refers to the number of balls and board games mentioned in the premise
if balls_premise != balls_hypothesis:
    # check if the number of balls in the hypothesis contradicts the number of balls reported in the premise
    label = "contradiction"
elif board_games_premise != board_games_hypothesis:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
