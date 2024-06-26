balls_premise = 4
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of balls and board games in the toy store, referenced also in the premise
if balls_hypothesis >= balls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls less than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
