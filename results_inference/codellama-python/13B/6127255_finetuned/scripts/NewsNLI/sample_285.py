points_difference_premise = 15
points_difference_hypothesis = 15

# the hypothesis mentions the points difference in each Spurs victory, which is also mentioned in the premise
if points_difference_hypothesis!= points_difference_premise:
    # check if the points difference in the hypothesis contradicts the points difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
