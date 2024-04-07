# Premise: Carlos is more than 1 years old.
# Hypothesis: Carlos is 8 years old.
# Golden Label: neutral

age_carlos_premise = 1
age_carlos_hypothesis = 8

# the hypothesis provides a specific age for Carlos, who is also mentioned in the premise
if age_carlos_hypothesis <= age_carlos_premise:
    # check if the age provided in the hypothesis contradicts the estimate of more than 'age_carlos_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Carlos' age
    # any age greater than 'age_carlos_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

