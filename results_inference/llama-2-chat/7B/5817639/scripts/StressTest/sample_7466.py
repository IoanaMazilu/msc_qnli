balls_premise = 3
board_games_premise = 6
balls_hypothesis = 2
board_games_hypothesis = 4

# the hypothesis talks about the number of balls and board games in the toy store, while the premise gives the total number of items
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis < board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
