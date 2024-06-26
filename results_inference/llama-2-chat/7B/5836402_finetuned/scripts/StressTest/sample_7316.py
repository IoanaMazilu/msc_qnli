stop_time_premise = 30
stop_time_hypothesis = 80

# the hypothesis refers to the time Jim stops, mentioned in the premise
if stop_time_premise!= stop_time_hypothesis:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
