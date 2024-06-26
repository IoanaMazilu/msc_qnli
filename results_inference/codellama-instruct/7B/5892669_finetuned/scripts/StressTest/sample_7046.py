travel_time_premise = 10
travel_time_hypothesis = 10

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the estimate of 'travel_time_hypothesis' contradicts the travel time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
