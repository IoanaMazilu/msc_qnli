james_hours_worked_premise = 41
james_hours_worked_hypothesis = 71

# the hypothesis refers to the number of hours James worked last week, mentioned also in the premise
if james_hours_worked_hypothesis <= james_hours_worked_premise:
    # check if the hypothesis value contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
