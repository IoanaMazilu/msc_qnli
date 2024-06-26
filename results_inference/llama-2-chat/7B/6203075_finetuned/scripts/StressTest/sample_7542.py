balls_premise = 3
balls_hypothesis = 5
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of types of balls and board games in the toy store
if balls_premise >= balls_hypothesis:
    # check if the number of 'balls_premise' contradicts the hypothesis
    label = "contradiction"
elif board_games_premise!= board_games_hypothesis:
    # check if the number of 'board_games_premise' contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)