distance_premise = 2
distance_hypothesis = 3

if distance_hypothesis!= distance_premise:
    # check if the distance they ran in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
