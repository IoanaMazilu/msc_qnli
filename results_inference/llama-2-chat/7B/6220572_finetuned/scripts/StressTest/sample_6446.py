frank_age_difference_premise = 14
frank_age_difference_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_hypothesis <= frank_age_difference_premise:
    # check if the estimate of 'frank_age_difference_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # any age difference greater than 'frank_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
