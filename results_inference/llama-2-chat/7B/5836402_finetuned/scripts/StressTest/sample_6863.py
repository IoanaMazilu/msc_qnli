distance_premise = 45
distance_hypothesis = 85

# the hypothesis refers to the distance traveled by Johnny after Matthew started waking from r to y, mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
