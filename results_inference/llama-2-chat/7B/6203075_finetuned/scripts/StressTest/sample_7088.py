work_hours_premise = 6
work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
