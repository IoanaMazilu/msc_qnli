frank_age_premise = 84
frank_age_hypothesis = 14

# the hypothesis talks about the age difference between Frank and John, referenced also in the premise
if frank_age_hypothesis <= frank_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'frank_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'frank_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
