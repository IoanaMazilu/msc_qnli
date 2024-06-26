distance_sisters_premise = 2
distance_sisters_hypothesis = 3

if distance_sisters_hypothesis!= distance_sisters_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)
