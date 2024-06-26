amanda_ball_premise = 1
amanda_board_games_premise = 3
amanda_ball_hypothesis = 2
amanda_board_games_hypothesis = 3

# the hypothesis talks about the number of items Amanda buys, referenced also in the premise
if amanda_ball_hypothesis <= amanda_ball_premise:
    # check if the hypothesis value contradicts the estimate of 'amanda_ball_premise'
    label = "contradiction"
elif amanda_board_games_hypothesis!= amanda_board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
