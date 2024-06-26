total_hours_worked_premise = 41
total_hours_worked_hypothesis = 71

# the hypothesis refers to the total number of hours worked by James, referenced also in the premise
if total_hours_worked_hypothesis <= total_hours_worked_premise:
    # check if the estimate of 'total_hours_worked_hypothesis' contradicts the total number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of hours worked
    # any number of hours greater than 'total_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
