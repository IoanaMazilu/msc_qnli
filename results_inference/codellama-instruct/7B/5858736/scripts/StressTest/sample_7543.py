balls_store_premise = 5
balls_hypothesis = 3
board_games_store_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of different selections of the 4 items that Amanda can make
if (balls_hypothesis + board_games_hypothesis) <= (balls_store_premise + board_games_store_premise):
    # check if the sum of the number of balls and board games in the hypothesis contradicts the estimate of less than 'balls_store_premise' and 'board_games_store_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of different selections of the 4 items that Amanda can make
    # any number of different selections greater than the estimate given in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
