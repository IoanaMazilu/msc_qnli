work_days_premise = 60
work_days_hypothesis = 60

# the hypothesis talks about the number of days Jhon works, referenced also in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the number of days Jhon works in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the number of days in the premise, we can infer entailment
    label = "entailment"

print(label)
