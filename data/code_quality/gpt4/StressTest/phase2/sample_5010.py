distance_premise = 270
distance_hypothesis = 470

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
