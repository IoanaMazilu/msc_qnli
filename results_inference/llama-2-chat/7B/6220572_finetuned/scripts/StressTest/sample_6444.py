frank_age_difference_premise = 14
frank_age_difference_hypothesis = 84

# the hypothesis talks about the age difference between Frank and John, also referenced in the premise
if frank_age_difference_hypothesis >= frank_age_difference_premise:
    # check if the hypothesis estimate contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'frank_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
