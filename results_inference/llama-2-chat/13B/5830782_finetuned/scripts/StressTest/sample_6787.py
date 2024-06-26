james_hours_worked_premise = 21
james_hours_worked_hypothesis = 41

# the hypothesis talks about the number of hours James worked last week, referenced also in the premise
if james_hours_worked_hypothesis <= james_hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'james_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked
    # any number of hours greater than 'james_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
