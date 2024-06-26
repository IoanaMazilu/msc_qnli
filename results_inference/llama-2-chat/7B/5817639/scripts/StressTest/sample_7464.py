balls_premise = 3
board_games_premise = 6
balls_hypothesis = 4
board_games_hypothesis = 6

# the hypothesis talks about the number of types of balls and board games in the toy store
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis <= board_games_premise:
    # check if the hypothesis value contradicts the estimate of 'board_games_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
