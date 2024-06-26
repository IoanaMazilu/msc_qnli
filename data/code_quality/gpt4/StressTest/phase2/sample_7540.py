balls_premise = 6
balls_hypothesis = 1
board_games_premise = 3
board_games_hypothesis = 3

# The hypothesis talks about the number of balls and board games Amanda buys, referenced also in the premise
if balls_hypothesis >= balls_premise:
    # check if the number of balls in the hypothesis contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis != board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
