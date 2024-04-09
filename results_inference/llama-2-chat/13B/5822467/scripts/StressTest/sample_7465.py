balls_premise = 4
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of balls and board games in the toy store
if balls_hypothesis <= balls_premise and board_games_hypothesis == board_games_premise:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
elif balls_hypothesis!= balls_premise or board_games_hypothesis!= board_games_premise:
    # check if the hypothesis values or estimates contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls and board games
    # any number of balls and board games consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
