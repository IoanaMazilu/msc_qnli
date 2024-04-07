# Premise: Amanda goes to the toy store to buy less than 4 ball and 3 different board games.
# Hypothesis: Amanda goes to the toy store to buy 1 ball and 3 different board games.
# Golden Label: neutral

balls_bought_premise = 4
balls_bought_hypothesis = 1
board_games_bought_premise = 3
board_games_bought_hypothesis = 3

# the hypothesis refers to the number of balls and board games bought by Amanda mentioned in the premise
if balls_bought_hypothesis >= balls_bought_premise:
    # check if the number of balls in the hypothesis contradicts the estimate of less than 'balls_bought_premise'
    label = "contradiction"
elif board_games_bought_hypothesis != board_games_bought_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

