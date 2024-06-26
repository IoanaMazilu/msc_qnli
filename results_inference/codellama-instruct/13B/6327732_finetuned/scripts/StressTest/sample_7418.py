molly_age_premise = 18
molly_age_hypothesis = 18

# the hypothesis refers to the number of years Molly will be more than 18 years old
if molly_age_hypothesis <= molly_age_premise:
    # check if the hypothesis value contradicts the estimate of more than'molly_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years Molly will be more than 18 years old
    # any number of years greater than'molly_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
