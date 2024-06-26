work_days_premise = 60
work_days_hypothesis = 60

# the hypothesis refers to the number of days Jhon works, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
