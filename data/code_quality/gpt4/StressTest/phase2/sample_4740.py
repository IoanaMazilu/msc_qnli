distance_premise = 50
distance_hypothesis = 80

# the hypothesis refers to the distance between the homes mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis estimate contradicts the exact distance given in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the hypothesis estimate contradicts the exact distance given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
