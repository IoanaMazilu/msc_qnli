hours_worked_premise = 60
hours_worked_hypothesis = 40

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hours_worked_hypothesis < hours_worked_premise:
    # if the number of hours worked in the hypothesis is less than the number of hours worked in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
