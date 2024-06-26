dan_work_hours_premise = 3
dan_work_hours_hypothesis = 4

# the hypothesis refers to the number of hours Dan works, which is also mentioned in the premise
if dan_work_hours_hypothesis!= dan_work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours Dan works in the premise
    label = "contradiction"
else:
    # if the number of hours Dan works in the hypothesis matches the number of hours Dan works in the premise, we can infer entailment
    label = "entailment"

print(label)
