balls_store_premise = 4
balls_hypothesis = 3
board_games_store_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of different selections T of the 4 items that Amanda can make
if balls_hypothesis <= balls_store_premise and board_games_hypothesis <= board_games_store_premise:
    # check if the estimate of 'balls_hypothesis' and 'board_games_hypothesis' contradicts the number of items in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items
    # any number of selections greater than 'balls_store_premise' and 'board_games_store_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
