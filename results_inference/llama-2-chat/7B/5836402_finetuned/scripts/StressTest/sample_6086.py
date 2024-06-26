work_days_premise = 20
work_days_hypothesis = 30

# the hypothesis refers to the number of days mentioned in the premise
if work_days_premise!= work_days_hypothesis:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
