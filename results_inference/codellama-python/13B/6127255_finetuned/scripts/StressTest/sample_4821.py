balls_bought_premise = 1
balls_bought_hypothesis = 2
board_games_bought_premise = 3
board_games_bought_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda buys, which is also mentioned in the premise
if balls_bought_hypothesis <= balls_bought_premise:
    # check if the hypothesis value contradicts the number of balls bought in the premise
    label = "contradiction"
elif board_games_bought_hypothesis!= board_games_bought_premise:
    # check if the number of board games bought in the hypothesis contradicts the number of board games bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
