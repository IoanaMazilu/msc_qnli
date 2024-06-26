work_days_premise = 8
work_days_hypothesis = 7

# the hypothesis refers to the number of days taken to complete the work, which is also mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
