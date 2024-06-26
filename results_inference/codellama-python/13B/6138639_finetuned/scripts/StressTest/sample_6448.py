john_age_difference_premise = 8
john_age_difference_hypothesis = 5

# the hypothesis talks about the number of years until John will be twice as old as Frank, referenced also in the premise
if john_age_difference_hypothesis >= john_age_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_age_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'john_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
