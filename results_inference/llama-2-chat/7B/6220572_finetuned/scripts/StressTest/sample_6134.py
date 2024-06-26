x_hours_premise = 40
x_hours_hypothesis = 40

# the hypothesis talks about the number of hours worked per week, referenced also in the premise
if x_hours_hypothesis >= x_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'x_hours_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'x_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
