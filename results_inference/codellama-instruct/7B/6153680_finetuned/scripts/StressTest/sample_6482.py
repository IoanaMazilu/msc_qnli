balls_premise = 3
balls_hypothesis = 1
games_premise = 6
games_hypothesis = 6

# the hypothesis refers to the same toy store as the premise
if balls_hypothesis!= balls_premise:
    # check if the number of balls in the hypothesis contradicts the number of balls in the premise
    label = "contradiction"
elif games_hypothesis!= games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
