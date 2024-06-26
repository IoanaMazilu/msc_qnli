dan_work_hours_premise = 3
dan_work_hours_hypothesis = 2

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_premise <= dan_work_hours_hypothesis:
    # check if the estimate of 'dan_work_hours_hypothesis' contradicts the number of hours Dan works in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
