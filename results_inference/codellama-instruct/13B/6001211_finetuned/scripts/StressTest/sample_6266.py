dan_work_hours_premise = 3
dan_work_hours_hypothesis = 4

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_premise!= dan_work_hours_hypothesis:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
