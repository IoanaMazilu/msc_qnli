x_premise = 10
x_hypothesis = 10

# the hypothesis talks about the number of hours worked per week
if x_hypothesis <= 70:
    # check if the hypothesis value contradicts the estimate of less than 70 hours
    label = "contradiction"
elif x_hypothesis <= 40:
    # check if the hypothesis value contradicts the estimate of less than 40 hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per week
    # any number of hours worked per week greater than 40 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
