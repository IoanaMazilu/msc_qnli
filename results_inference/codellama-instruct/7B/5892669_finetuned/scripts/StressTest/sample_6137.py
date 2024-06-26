hours_worked_james_premise = 41
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked, mentioned in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)
