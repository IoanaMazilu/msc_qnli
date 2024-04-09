points_premise = 0
points_hypothesis = 0

# the hypothesis mentions the same condition as the premise
if points_hypothesis!= points_premise:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
