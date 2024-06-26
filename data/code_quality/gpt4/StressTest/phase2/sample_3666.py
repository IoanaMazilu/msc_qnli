travel_time_premise = 11
travel_time_hypothesis = 61

# the hypothesis refers to the travel time of Pavan mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the estimate of 'travel_time_premise' contradicts the maximum travel time in the hypothesis
    label = "contradiction"
elif travel_time_premise < travel_time_hypothesis:
    # if the premise travel time is less than the maximum travel time in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
