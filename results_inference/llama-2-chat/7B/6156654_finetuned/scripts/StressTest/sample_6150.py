hours_worked_james_premise = 41
hours_worked_james_hypothesis = 71

# the hypothesis refers to the number of hours worked by James, which is also mentioned in the premise
if hours_worked_james_hypothesis < hours_worked_james_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the number of hours worked by James in the hypothesis does not contradict the number of hours worked by James in the premise, we can infer entailment
    label = "entailment"

print(label)
