balls_store_premise = 3
balls_store_hypothesis = 2
board_games_store_premise = 6
board_games_store_hypothesis = 6

# the hypothesis talks about the number of different selections of the 4 items that Amanda can make
if (balls_store_premise + board_games_store_premise) <= (balls_store_hypothesis + board_games_store_hypothesis):
    # check if the hypothesis value contradicts the estimate of more than 'balls_store_premise + board_games_store_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of different selections of the 4 items that Amanda can make
    # any number of different selections greater than 'balls_store_premise + board_games_store_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
