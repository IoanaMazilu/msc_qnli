balls_premise = 6
balls_hypothesis = 1
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis refers to the number of ball and board games Amanda buys
if balls_hypothesis >= balls_premise:
    # check if the hypothesis value contradicts the premise value for 'balls'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the hypothesis value contradicts the premise value for 'board games'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
