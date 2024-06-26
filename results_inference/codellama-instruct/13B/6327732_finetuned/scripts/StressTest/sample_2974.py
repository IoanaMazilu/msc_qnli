hours_premise = 85
hours_hypothesis = 15

# the hypothesis refers to the number of hours required to complete a job alone
if hours_hypothesis >= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours required to complete a job alone
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
