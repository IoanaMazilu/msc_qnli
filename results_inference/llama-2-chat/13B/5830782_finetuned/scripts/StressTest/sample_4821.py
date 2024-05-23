balls_premise = 1
balls_hypothesis = 2
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda buys, which is also mentioned in the premise
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the number of balls Amanda buys in the premise
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games Amanda buys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)