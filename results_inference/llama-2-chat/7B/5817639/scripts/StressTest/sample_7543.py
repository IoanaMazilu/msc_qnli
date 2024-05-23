balls_premise = 5
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of types of balls and board games in a toy store, referenced also in the premise
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of types of board games in the hypothesis contradicts the number of types of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)