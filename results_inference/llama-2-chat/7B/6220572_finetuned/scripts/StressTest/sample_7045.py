hours_travelled_premise = 20
hours_travelled_hypothesis = 10

# the hypothesis talks about the number of hours Raman travelled, referenced also in the premise
if hours_travelled_hypothesis >= hours_travelled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_travelled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
