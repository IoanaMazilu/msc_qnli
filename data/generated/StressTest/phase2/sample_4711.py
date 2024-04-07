# Premise: After they have worked together for less than 82 days Matt stops and Peter completes the remaining work in 8 days.
# Hypothesis: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 8 days.
# Golden Label: neutral

working_days_together_premise = 82
working_days_together_hypothesis = 12
peter_remaining_work_days_premise = 8
peter_remaining_work_days_hypothesis = 8

# the hypothesis refers to the number of days they worked together and the days Peter worked alone mentioned in the premise
if working_days_together_hypothesis >= working_days_together_premise:
    # check if the number of 'working_days_together_hypothesis' contradicts the estimate of less than 'working_days_together_premise'
    label = "contradiction"
elif peter_remaining_work_days_hypothesis != peter_remaining_work_days_premise:
    # check if the number of 'peter_remaining_work_days_hypothesis' contradicts the number of remaining work days for Peter in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

