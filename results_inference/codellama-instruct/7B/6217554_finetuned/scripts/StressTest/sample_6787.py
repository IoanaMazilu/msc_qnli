total_hours_worked_premise = 21
total_hours_worked_hypothesis = 41

# the hypothesis talks about the total number of hours worked by James, referenced also in the premise
if total_hours_worked_hypothesis <= total_hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of hours worked
    # any number of hours greater than 'total_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
