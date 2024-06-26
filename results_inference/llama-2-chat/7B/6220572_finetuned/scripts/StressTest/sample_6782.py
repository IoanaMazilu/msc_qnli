x_hours_premise = 30
x_hours_hypothesis = 80

# the hypothesis refers to the number of hours worked per week, referenced also in the premise
if x_hours_hypothesis <= x_hours_premise:
    # check if the estimate of 'x_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours greater than 'x_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
