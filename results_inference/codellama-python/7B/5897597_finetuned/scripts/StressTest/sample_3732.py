travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the travel time in the premise contradicts the estimate of less than 'travel_time_hypothesis'
    label = "contradiction"
else:
    # if the travel time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
