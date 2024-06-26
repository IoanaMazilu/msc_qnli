age_premise = 18
age_hypothesis = 24

# the hypothesis refers to Molly's age in the future, while the premise refers to her age 6 years ago
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the number of years since the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's age 6 years ago
    # any number of years greater than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
