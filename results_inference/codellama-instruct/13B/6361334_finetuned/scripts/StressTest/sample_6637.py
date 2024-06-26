work_days_premise = 50
work_days_hypothesis = 30

# the hypothesis refers to the number of days it takes to complete a work, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
