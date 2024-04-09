balls_premise = 1
balls_hypothesis = 7
board_games_premise = 3
board_games_hypothesis = 3

# the hypothesis talks about the number of ball and board games Amanda goes to buy
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
