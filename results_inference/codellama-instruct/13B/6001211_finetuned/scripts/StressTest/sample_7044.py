travel_time_premise = 10
travel_time_hypothesis = 20

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the estimate of 'travel_time_premise' contradicts the travel time in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
