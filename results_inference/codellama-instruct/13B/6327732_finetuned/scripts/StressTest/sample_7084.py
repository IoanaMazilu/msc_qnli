hours_premise = 20
hours_hypothesis = 10

# the hypothesis refers to the number of hours required to complete a job, mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours required to complete a job
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
