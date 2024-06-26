points_premise = 500
points_hypothesis = -500

# the hypothesis and premise mention the points change of SENSEX
if points_hypothesis!= points_premise:
    # check if the points change in the hypothesis contradicts the points change in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
