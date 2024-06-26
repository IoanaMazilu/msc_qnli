james_hours_worked_premise = 21
james_hours_worked_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_hours_worked_hypothesis <= james_hours_worked_premise:
    # check if the number of hours James worked last week according to the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked last week
    # any number of hours greater than 'james_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
