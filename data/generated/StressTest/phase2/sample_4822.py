# Premise: Amanda goes to the toy store to buy less than 2 ball and 3 different board games.
# Hypothesis: Amanda goes to the toy store to buy 1 ball and 3 different board games.
# Golden Label: neutral

ball_buy_premise = 2
ball_buy_hypothesis = 1
board_games_buy_premise = 3
board_games_buy_hypothesis = 3

# The hypothesis refers to the number of balls and board games Amanda buys, which is also mentioned in the premise
if ball_buy_hypothesis >= ball_buy_premise:
    # check if the number of balls Amanda buys in the hypothesis contradicts the estimate of less than 'ball_buy_premise' in the premise
    label = "contradiction"
elif board_games_buy_hypothesis != board_games_buy_premise:
    # check if the number of board games Amanda buys in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

