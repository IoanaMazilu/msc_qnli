hours_worked_premise = 10
hours_worked_hypothesis = 30

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the premise
    label = "contradiction"
elif hours_worked_hypothesis > hours_worked_premise:
    # if the number of hours worked in the hypothesis is greater than the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of hours worked in the hypothesis is equal to the premise, we can infer neutrality
    label = "neutral"

print(label)
