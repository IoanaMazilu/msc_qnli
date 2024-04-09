travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis refers to the travel time from A to B and back mentioned in the premise
if travel_time_premise > travel_time_hypothesis:
    # check if the premise travel time contradicts the hypothesis estimate of less than 'travel_time_hypothesis'
    label = "contradiction"
elif travel_time_premise < travel_time_hypothesis:
    # if the premise travel time is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # if the premise travel time equals the hypothesis estimate, it is neutral as it does not contradict but cannot be explicitly entailed
    label = "neutral"

print(label)
