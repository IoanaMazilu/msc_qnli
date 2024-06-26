distance_matthew_premise = 35
distance_matthew_hypothesis = 45

# the hypothesis talks about the distance Matthew walked, which is also mentioned in the premise
if distance_matthew_hypothesis!= distance_matthew_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is equal to the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
