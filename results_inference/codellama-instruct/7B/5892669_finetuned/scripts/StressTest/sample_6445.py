age_difference_premise = 84
age_difference_hypothesis = 14

# the hypothesis talks about the age difference between Frank and John, referenced also in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
