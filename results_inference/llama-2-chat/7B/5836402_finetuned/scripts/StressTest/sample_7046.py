travel_time_premise = 10
travel_time_hypothesis = 10

# the hypothesis refers to the duration of Raman's travel mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the estimate of 'travel_time_hypothesis' contradicts the travel duration in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
