points_premise = 15
points_hypothesis = 15

# the hypothesis mentions the number of points by which each Spurs victory was achieved, which is also referenced in the premise
if points_hypothesis!= points_premise:
    # check if the number of points in the hypothesis contradicts the number of points reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
