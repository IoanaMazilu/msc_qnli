travel_distance_premise = 1800
travel_distance_hypothesis = 7800

# the hypothesis refers to the same travel distance mentioned in the premise
if travel_distance_premise!= travel_distance_hypothesis:
    # check if the travel distance in the hypothesis contradicts the travel distance reported in the premise
    label = "contradiction"
else:
    # if the travel distance in the hypothesis does not contradict the travel distance in the premise, we can infer entailment
    label = "entailment"

print(label)
