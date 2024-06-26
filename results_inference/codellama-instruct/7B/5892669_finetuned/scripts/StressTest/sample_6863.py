distance_premise = 45
distance_hypothesis = 85

# the hypothesis refers to the same event mentioned in the premise
if distance_premise!= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
