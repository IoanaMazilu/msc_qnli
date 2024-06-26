travel_time_premise = 7
travel_time_hypothesis = 5

# the hypothesis refers to the total travel time mentioned in the premise
if travel_time_premise < travel_time_hypothesis:
    # check if the given 'travel_time_premise' contradicts the estimate of more than 'travel_time_hypothesis' hours
    label = "contradiction"
elif travel_time_premise == travel_time_hypothesis:
    # check if the 'travel_time_premise' equals the 'travel_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
