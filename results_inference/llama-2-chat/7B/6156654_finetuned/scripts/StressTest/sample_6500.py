distance_matthew = 45
distance_hypothesis = 45

# the hypothesis refers to the distance Matthew walked, which is also mentioned in the premise
if distance_hypothesis!= distance_matthew:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
