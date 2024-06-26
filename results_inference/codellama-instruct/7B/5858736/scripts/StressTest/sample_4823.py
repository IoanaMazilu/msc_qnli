balls_bought_premise = 1
board_games_bought_premise = 3

# the hypothesis refers to the number of balls and board games mentioned in the premise
if balls_bought_premise >= 1 and board_games_bought_premise >= 3:
    # check if the estimate of 'balls_bought_hypothesis' contradicts the number of balls bought in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls and board games
    # any number of balls and board games less than 1 and 3, respectively, is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
