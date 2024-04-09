less_than_premise = 20
less_than_hypothesis = 10

# the hypothesis talks about the duration of Raman's travel, referenced also in the premise
if less_than_hypothesis <= less_than_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of Raman's travel
    # any duration less than 'less_than_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
