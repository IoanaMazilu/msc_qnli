hours_worked_james_premise = 41
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, mentioned also in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
