hours_worked_james_premise = 42
hours_worked_james_hypothesis = 62

# the hypothesis refers to the number of hours James worked last week mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the estimate of 'hours_worked_james_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
