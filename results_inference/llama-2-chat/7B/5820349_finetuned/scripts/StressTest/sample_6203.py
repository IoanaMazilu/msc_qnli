travel_distance_premise = 200
travel_distance_hypothesis = 200

# the hypothesis refers to the travel distance mentioned in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
