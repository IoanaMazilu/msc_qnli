# Premise: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for less than 52 days Matt stops and Peter completes the remaining work in 10 days.
# Golden Label: entailment

work_together_days_premise = 12
work_together_days_hypothesis = 52
peter_work_days_premise = 10
peter_work_days_hypothesis = 10

# the hypothesis refers to the number of days they worked together and the number of days Peter worked alone, mentioned in the premise
if work_together_days_premise >= work_together_days_hypothesis:
    # check if the estimate of 'work_together_days_hypothesis' contradicts the number of days they worked together in the premise
    label = "contradiction"
elif peter_work_days_hypothesis != peter_work_days_premise:
    # check if the number of days Peter worked alone in the hypothesis contradicts the number of days he worked alone reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

