james_worked_hours_premise = 41
harry_worked_hours_hypothesis = james_worked_hours_premise

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_worked_hours_hypothesis >= james_worked_hours_premise:
    # check if the hypothesis value contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the number of hours James worked in the premise, it is consistent with the premise
    label = "entailment"

print(label)
