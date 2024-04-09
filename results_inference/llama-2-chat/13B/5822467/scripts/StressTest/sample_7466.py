balls_premise = 3
balls_hypothesis = 2
board_games_premise = 6
board_games_hypothesis = 4

# the hypothesis talks about the number of balls and board games in the toy store
if balls_hypothesis <= balls_premise and board_games_hypothesis <= board_games_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif balls_hypothesis!= balls_premise or board_games_hypothesis!= board_games_premise:
    # check if the number of balls or board games in the hypothesis contradicts the number of balls or board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
