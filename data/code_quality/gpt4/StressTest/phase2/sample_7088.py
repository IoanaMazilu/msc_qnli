dan_work_hours_premise = 6
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
