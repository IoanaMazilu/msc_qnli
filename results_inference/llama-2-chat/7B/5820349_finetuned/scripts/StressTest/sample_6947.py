travel_time_premise = 7
travel_time_hypothesis = 7

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the estimate of 'travel_time_hypothesis' contradicts the travel time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
