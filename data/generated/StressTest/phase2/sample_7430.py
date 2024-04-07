# Premise: Amanda goes to the toy store to buy 1 ball and 3 different board games.
# Hypothesis: Amanda goes to the toy store to buy 7 ball and 3 different board games.
# Golden Label: contradiction

balls_premise = 1
balls_hypothesis = 7
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of balls and board games mentioned in the premise
if balls_hypothesis != balls_premise:
    # check if the number of balls in the hypothesis contradicts the number of balls mentioned in the premise
    label = "contradiction"
elif board_games_hypothesis != board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
