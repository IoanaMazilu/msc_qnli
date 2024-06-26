ball_types_premise = 4
ball_types_hypothesis = 3
board_game_types_premise = 6
board_game_types_hypothesis = 6

# the hypothesis talks about the types of balls and board games in the toy store, referenced also in the premise
if ball_types_hypothesis >= ball_types_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ball_types_premise'
    label = "contradiction"
elif board_game_types_hypothesis != board_game_types_premise:
    # check if the number of board game types in the hypothesis contradicts the number of board game types reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
