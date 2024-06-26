balls_store_premise = 3
board_games_store_premise = 6
balls_store_hypothesis = 4
board_games_store_hypothesis = 6

# the hypothesis refers to the number of different selections Amanda can make with the 4 items, referenced also in the premise
if balls_store_hypothesis <= balls_store_premise and board_games_store_hypothesis <= board_games_store_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_store_premise' and 'board_games_store_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of different selections Amanda can make
    # any number of selections greater than 'balls_store_premise' and 'board_games_store_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
