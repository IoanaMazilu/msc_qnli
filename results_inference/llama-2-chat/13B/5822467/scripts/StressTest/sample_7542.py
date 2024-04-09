ball_types_premise = 3
ball_types_hypothesis = 5
board_games_premise = 6

# the hypothesis talks about the number of ball types and board games, referenced also in the premise
if ball_types_hypothesis <= ball_types_premise and board_games_premise == board_games_hypothesis:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
elif ball_types_hypothesis > ball_types_premise or board_games_hypothesis!= board_games_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of ball types and board games
    # any number of ball types and board games less than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
