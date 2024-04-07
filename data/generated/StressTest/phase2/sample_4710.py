# Premise: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 8 days.
# Hypothesis: After they have worked together for less than 82 days Matt stops and Peter completes the remaining work in 8 days.
# Golden Label: entailment

work_together_days_premise = 12
work_together_days_hypothesis = 82
work_remaining_days_peter = 8

# the hypothesis refers to the number of days they worked together and the remaining days Peter worked, mentioned in the premise
if work_together_days_hypothesis < work_together_days_premise:
    # check if the estimate of 'work_together_days_hypothesis' contradicts the number of days they worked together in the premise
    label = "contradiction"
elif work_remaining_days_peter != 8:
    # check if the number of remaining days Peter worked in the hypothesis contradicts the number of remaining days Peter worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

