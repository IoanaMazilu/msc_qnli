points_premise = 15
points_hypothesis = 15

# the hypothesis mentions the points margin for each Spurs victory, which is also referenced in the premise
if points_hypothesis!= points_premise:
    # check if the points margin in the hypothesis contradicts the points margin reported in the premise
    label = "contradiction"
else:
    # if the hypothesis points do not contradict the premise points, we can infer entailment
    label = "entailment"

print(label)
