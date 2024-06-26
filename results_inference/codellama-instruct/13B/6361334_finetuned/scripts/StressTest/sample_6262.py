hours_premise = 40
hours_hypothesis = 10

# the hypothesis refers to the number of hours required to complete a job, mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours required to complete a job
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)