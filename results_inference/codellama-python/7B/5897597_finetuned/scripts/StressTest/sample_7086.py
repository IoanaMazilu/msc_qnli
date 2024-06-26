dan_work_hours_premise = 6
dan_work_hours_hypothesis = 8

# the hypothesis refers to the number of hours Dan works, which is also mentioned in the premise
if dan_work_hours_hypothesis <= dan_work_hours_premise:
    # check if the hypothesis value contradicts the number of hours Dan works in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
