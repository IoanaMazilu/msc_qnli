balls_premise = 1 + 2 + 3  # more than 1 type of balls
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of balls and board games, referenced also in the premise
if balls_hypothesis <= balls_premise and board_games_hypothesis == board_games_premise:
    # check if the hypothesis values for balls and board games contradict the premise values
    label = "contradiction"
elif balls_hypothesis!= balls_premise or board_games_hypothesis!= board_games_premise:
    # check if the hypothesis values for balls and board games contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls and board games
    # any number of balls and board games consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
