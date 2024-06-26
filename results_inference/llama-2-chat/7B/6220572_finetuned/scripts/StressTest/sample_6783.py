x_hours_premise = 40
x_hours_hypothesis = 70

# the hypothesis refers to the number of hours worked per week, mentioned in the premise
if x_hours_hypothesis <= x_hours_premise:
    # check if the hypothesis estimate contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'x_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
