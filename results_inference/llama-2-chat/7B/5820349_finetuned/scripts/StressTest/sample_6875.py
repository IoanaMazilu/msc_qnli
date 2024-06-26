work_days_premise = 60
work_days_hypothesis = 60

# the hypothesis refers to the number of days Jhon works, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the number of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
