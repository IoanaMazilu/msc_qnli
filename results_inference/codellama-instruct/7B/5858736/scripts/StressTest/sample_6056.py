# the hypothesis refers to the total time spent jogging and walking, while the premise only mentions the total time
if total_time_hypothesis <= total_time_premise:
    # check if the estimate of 'total_time_hypothesis' contradicts the total time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
