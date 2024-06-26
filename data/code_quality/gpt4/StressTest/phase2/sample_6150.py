james_hours_worked_premise = 41
james_hours_worked_hypothesis = 71

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_hours_worked_hypothesis <= james_hours_worked_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James mentioned in the premise
    label = "contradiction"
elif james_hours_worked_hypothesis > james_hours_worked_premise:
    # the premise gives the exact number of hours James worked last week
    # any number of hours less than 'james_hours_worked_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the number of hours worked by James in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
