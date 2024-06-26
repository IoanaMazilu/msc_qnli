age_premise = 18
age_hypothesis = 25

# the hypothesis refers to Molly's age in the future, while the premise refers to her age 7 years ago
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the number of years since 'age_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for Molly's age 7 years ago, while the hypothesis refers to her age in the future
    # any age greater than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
