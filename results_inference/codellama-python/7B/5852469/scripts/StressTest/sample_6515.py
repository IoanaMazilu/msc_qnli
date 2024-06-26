john_age_premise = 6
john_age_hypothesis = 10

# the hypothesis refers to the age of John, referenced also in the premise
if john_age_hypothesis <= john_age_premise:
    # check if the estimate of 'john_age_hypothesis' contradicts the age of John in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of John
    # any age greater than 'john_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
