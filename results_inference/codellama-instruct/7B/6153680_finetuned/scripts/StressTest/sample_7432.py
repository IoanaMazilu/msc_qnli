balls_premise = 1
balls_hypothesis = 3
games_premise = 6
games_hypothesis = 6

# the hypothesis talks about the number of balls and board games in the toy store, which is also mentioned in the premise
if balls_hypothesis > balls_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif games_hypothesis!= games_premise:
    # check if the number of board games in the hypothesis contradicts the number of board games in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
