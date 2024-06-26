diana_age_difference_premise = 3
diana_age_difference_hypothesis = 4

# the hypothesis talks about the age difference between Diana and Rashid, referenced also in the premise
if diana_age_difference_hypothesis <= diana_age_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'diana_age_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'diana_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
