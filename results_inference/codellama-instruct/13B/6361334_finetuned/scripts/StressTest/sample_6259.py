hours_premise = 25
hours_hypothesis = 15

# the hypothesis refers to the number of hours Dan can do a job alone, which is also mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours Dan can do a job alone
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
