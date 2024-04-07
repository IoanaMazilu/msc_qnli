# Premise: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 8 days.
# Hypothesis: After they have worked together for less than 12 days Matt stops and Peter completes the remaining work in 8 days.
# Golden Label: contradiction

work_together_days_premise = 12
work_together_days_hypothesis = 12
peter_work_days_premise = 8
peter_work_days_hypothesis = 8

# the hypothesis refers to the number of days they worked together and the number of days Peter worked, mentioned in the premise
if work_together_days_hypothesis >= work_together_days_premise:
    # check if the estimate of 'work_together_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif peter_work_days_hypothesis != peter_work_days_premise:
    # check if the number of days Peter worked in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

