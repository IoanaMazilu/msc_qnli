balls_premise = 3
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis talks about the number of types of balls and board games in the toy store, which are also mentioned in the premise
if balls_hypothesis >= balls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
elif board_games_hypothesis!= board_games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
