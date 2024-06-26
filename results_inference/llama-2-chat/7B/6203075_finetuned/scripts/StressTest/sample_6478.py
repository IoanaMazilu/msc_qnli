balls_premise = 4
balls_hypothesis = 1
games_premise = 3
games_hypothesis = 3

# the hypothesis refers to the number of balls and board games Amanda buys, which are also mentioned in the premise
if balls_hypothesis >= balls_premise:
    # check if the number of balls in the hypothesis contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
elif games_hypothesis!= games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
