work_days_premise = 50
work_days_hypothesis = 30

# the hypothesis refers to the number of days needed to complete a work, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise estimate, we can infer entailment
    label = "entailment"

print(label)
