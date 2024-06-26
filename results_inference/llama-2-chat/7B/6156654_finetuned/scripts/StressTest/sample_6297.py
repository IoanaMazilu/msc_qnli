hours_worked_premise = 12
hours_worked_hypothesis = 82

# the hypothesis refers to the number of hours Harry works per week, which is also mentioned in the premise
if hours_worked_premise > hours_worked_hypothesis:
    # check if the number of hours Harry works in the premise contradicts the estimate of less than 'hours_worked_hypothesis' in the hypothesis
    label = "contradiction"
elif hours_worked_premise == hours_worked_hypothesis:
    # check if the number of hours Harry works in the premise is equal to the estimate in the hypothesis
    label = "neutral"
else:
    # if the number of hours Harry works in the premise is less than 'hours_worked_hypothesis', we can infer entailment
    label = "entailment"

print(label)
