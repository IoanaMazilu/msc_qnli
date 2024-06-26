work_hours_premise = 6
work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, referenced also in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
