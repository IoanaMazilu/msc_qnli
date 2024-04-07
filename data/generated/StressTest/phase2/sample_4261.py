# Premise: Frank is less than 25 years younger then John.
# Hypothesis: Frank is 15 years younger then John.
# Golden Label: neutral

age_difference_premise = 25
age_difference_hypothesis = 15

# The hypothesis states a specific age difference between Frank and John, also referenced in the premise
if age_difference_hypothesis > age_difference_premise:
    # Check if the hypothesis age difference contradicts the premise's estimate of less than 'age_difference_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the age difference
    # Any age difference less than or equal to 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

