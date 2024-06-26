balls_store_premise = 1
board_games_store_premise = 6
balls_hypothesis = 3
board_games_hypothesis = 6

# the hypothesis talks about the number of different selections R of the 4 items that Amanda can make
if balls_hypothesis <= balls_store_premise and board_games_hypothesis <= board_games_store_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of different selections R
    # any number of selections greater than 'R' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
