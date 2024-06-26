balls_premise = 1
balls_hypothesis = 6
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda buys, mentioned in the premise
if balls_premise >= balls_hypothesis:
    # check if the number of balls in the premise contradicts the estimate of less than 'balls_hypothesis'
    label = "contradiction"
elif board_games_premise!= board_games_hypothesis:
    # check if the number of board games in the premise contradicts the number of board games in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
