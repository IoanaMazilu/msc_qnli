hours_worked_james_premise = 41
hours_worked_james_hypothesis = 21

# the hypothesis refers to the number of hours James worked last week, as mentioned in the premise
if hours_worked_james_hypothesis != hours_worked_james_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
