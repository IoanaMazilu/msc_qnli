age_difference_premise = 6
age_difference_hypothesis = 7

# the hypothesis talks about the age difference between Kiran and Bineesh, referenced also in the premise
if age_difference_hypothesis <= age_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
