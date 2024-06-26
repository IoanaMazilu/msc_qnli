frank_age_premise = 84
frank_age_hypothesis = 14

# the hypothesis refers to the age difference between Frank and John
if frank_age_hypothesis >= frank_age_premise:
    # check if the estimate of 'frank_age_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the age difference
    # any age difference less than 'frank_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
