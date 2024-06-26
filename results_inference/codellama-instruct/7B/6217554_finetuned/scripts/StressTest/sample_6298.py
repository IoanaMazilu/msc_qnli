x_hour_premise = 82
x_hour_hypothesis = 12

# the hypothesis talks about the number of hours Harry works, referenced also in the premise
if x_hour_hypothesis >= x_hour_premise:
    # check if the number of hours Harry works in the hypothesis contradicts the number of hours mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Harry works
    # any number of hours less than 'x_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
