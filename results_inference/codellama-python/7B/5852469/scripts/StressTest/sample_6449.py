john_age_premise = 5
john_age_hypothesis = 7

# the hypothesis refers to the number of years in the premise
if john_age_hypothesis <= john_age_premise:
    # check if the estimate of 'john_age_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'john_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
