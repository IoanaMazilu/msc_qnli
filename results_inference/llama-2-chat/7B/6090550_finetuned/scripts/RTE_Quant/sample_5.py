distance_premise = 505
distance_hypothesis = 505

# the hypothesis mentions the distance from Scott Island to Victoria, which is also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis matches the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
