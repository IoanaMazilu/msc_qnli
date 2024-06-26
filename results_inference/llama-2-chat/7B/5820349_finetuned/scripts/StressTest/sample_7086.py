dan_work_hours_premise = 6
dan_work_hours_hypothesis = 8

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_premise >= dan_work_hours_hypothesis:
    # check if the estimate of 'dan_work_hours_premise' contradicts the number of hours Dan works in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
