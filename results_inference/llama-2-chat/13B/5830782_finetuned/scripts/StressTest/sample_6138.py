travel_time_premise = 7
travel_time_hypothesis = 4

# the hypothesis refers to the travel time from A to B and back mentioned in the premise
if travel_time_premise < travel_time_hypothesis:
    # check if the 'travel_time_premise' contradicts the estimate of more than 'travel_time_hypothesis'
    label = "contradiction"
elif travel_time_premise == travel_time_hypothesis:
    # check if the 'travel_time_premise' contradicts the estimate of more than 'travel_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
