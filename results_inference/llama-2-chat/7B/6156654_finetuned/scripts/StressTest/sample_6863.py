distance_matthew_premise = 45
distance_matthew_hypothesis = 85

# the hypothesis refers to the distance Matthew walked, which is also mentioned in the premise
if distance_matthew_hypothesis!= distance_matthew_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis matches the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
