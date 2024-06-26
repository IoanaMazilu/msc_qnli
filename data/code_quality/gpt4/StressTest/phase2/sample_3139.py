john_age_multiple_premise = 1
john_age_multiple_hypothesis = 3

# the hypothesis refers to the age ratio between John and Mark mentioned in the premise
if john_age_multiple_hypothesis <= john_age_multiple_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_age_multiple_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any multiple greater than 'john_age_multiple_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
