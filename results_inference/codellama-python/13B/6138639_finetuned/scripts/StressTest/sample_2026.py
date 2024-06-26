john_age_diff_premise = 5
john_age_diff_hypothesis = 6

# the hypothesis talks about the age difference between John and Tom, referenced also in the premise
if john_age_diff_hypothesis <= john_age_diff_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_age_diff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'john_age_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
