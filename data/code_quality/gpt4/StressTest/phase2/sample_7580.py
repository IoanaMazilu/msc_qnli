work_days_premise = 8
work_days_hypothesis = 8

# the hypothesis refers to the number of days to complete the work mentioned in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
