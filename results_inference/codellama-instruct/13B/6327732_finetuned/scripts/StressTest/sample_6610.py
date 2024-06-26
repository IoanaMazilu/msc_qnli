molly_age_premise = 88
molly_age_hypothesis = 18

# the hypothesis refers to Molly's age in 18 years, which is not explicitly mentioned in the premise
if molly_age_hypothesis <= molly_age_premise:
    # check if the hypothesis value contradicts the estimate of less than'molly_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's age
    # any number of years greater than'molly_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
