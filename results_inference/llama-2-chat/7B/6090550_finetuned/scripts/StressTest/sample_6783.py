hours_worked_premise = 40
hours_worked_hypothesis = 70

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hours_worked_hypothesis < hours_worked_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the number of hours in the hypothesis does not contradict the number of hours in the premise, we can infer entailment
    label = "entailment"

print(label)
