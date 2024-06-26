work_days_premise = 20
work_days_hypothesis = 40

# the hypothesis refers to the same work scenario as the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
