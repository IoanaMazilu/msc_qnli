travel_distance_premise = 200
travel_distance_hypothesis = 300

# the hypothesis refers to the travel distance mentioned in the premise
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the estimate of 'travel_distance_hypothesis' contradicts the number of travel distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
