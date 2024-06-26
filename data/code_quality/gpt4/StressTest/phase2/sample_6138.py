total_travel_time_premise = 7
total_travel_time_hypothesis = 4

# the hypothesis refers to the total time of travel mentioned in the premise
if total_travel_time_premise < total_travel_time_hypothesis:
    # check if the estimate of 'total_travel_time_hypothesis' contradicts the time of travel in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
