 score_premise = 2
score_hypothesis = 7

# the hypothesis refers to the score Jerry must earn on the fourth test to raise his average by a certain number of points, as mentioned in the premise
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
