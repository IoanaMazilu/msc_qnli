molly_age_premise = 18
molly_age_hypothesis = 88

# the hypothesis talks about the number of years Molly will be six times her age seven years ago
# the premise mentions Molly's age in 18 years, which is less than the hypothesis value
if molly_age_hypothesis <= molly_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's age
    # any number of years greater than'molly_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
