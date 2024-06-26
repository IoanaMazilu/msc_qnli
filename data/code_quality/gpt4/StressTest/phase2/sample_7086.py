dan_work_hours_premise = 6
dan_work_hours_hypothesis = 8

# the hypothesis refers to the number of hours Dan works alone, mentioned in the premise
if dan_work_hours_hypothesis < dan_work_hours_premise:
    # check if the estimate of 'dan_work_hours_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
elif dan_work_hours_hypothesis > dan_work_hours_premise:
    # check if the number of work hours in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
