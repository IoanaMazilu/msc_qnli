balls_premise = 4
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of different selections W of 4 items that Amanda can make in a toy store with less than 4 types of balls and 6 types of board games
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of different selections W of 4 items in the hypothesis contradicts the number of different selections reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
