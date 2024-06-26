hours_premise = 60
hours_hypothesis = 40

# the hypothesis refers to the number of hours James works per week, mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
