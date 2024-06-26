travel_time_premise = 10
travel_time_hypothesis = 20

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the travel time in the premise contradicts the estimate of less than 'travel_time_hypothesis'
    label = "contradiction"
else:
    # if the travel time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)