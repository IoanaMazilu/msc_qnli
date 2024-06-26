ball_types_premise = 4
ball_types_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of types of balls and board games in the toy store, referenced also in the premise
if ball_types_hypothesis >= ball_types_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ball_types_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of ball types
    # any number of ball types less than 'ball_types_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)