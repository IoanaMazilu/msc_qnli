# Premise: Amanda goes to the toy store to buy 1 ball and 3 different board games.
# Hypothesis: Amanda goes to the toy store to buy less than 2 ball and 3 different board games.
# Golden Label: entailment

balls_bought_premise = 1
balls_bought_hypothesis = 2
board_games_bought_premise = 3
board_games_bought_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda bought, mentioned in the premise
if balls_bought_hypothesis <= balls_bought_premise:
    # check if the estimate of 'balls_bought_hypothesis' contradicts the number of balls bought in the premise
    label = "contradiction"
elif board_games_bought_hypothesis != board_games_bought_premise:
    # check if the number of board games bought in the hypothesis contradicts the number of board games bought reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

