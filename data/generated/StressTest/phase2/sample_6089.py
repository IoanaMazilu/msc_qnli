# Premise: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for 72 days Matt stops and Peter completes the remaining work in 10 days.
# Golden Label: contradiction

work_together_premise = 12
work_together_hypothesis = 72
remaining_work_peter_premise = 10
remaining_work_peter_hypothesis = 10

# the hypothesis refers to the number of days they worked together and the remaining days Peter worked alone, mentioned in the premise
if work_together_premise != work_together_hypothesis:
    # check if the number of days they worked together in the hypothesis contradicts the number of days they worked together reported in the premise
    label = "contradiction"
elif remaining_work_peter_hypothesis != remaining_work_peter_premise:
    # check if the number of remaining work days for Peter in the hypothesis contradicts the number of remaining work days for Peter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

