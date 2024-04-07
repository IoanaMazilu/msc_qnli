# Premise: Frank is less than 75 years younger then John.
# Hypothesis: Frank is 15 years younger then John.
# Golden Label: neutral

age_difference_premise = 75
age_difference_hypothesis = 15

# the hypothesis states a specific age difference between Frank and John, which is also estimated in the premise
if age_difference_hypothesis > age_difference_premise:
    # check if the hypothesis age difference contradicts the maximum age difference stated in the premise
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # the premise gives only an estimate for the maximum age difference
    # any age difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis age difference matches the premise estimate, we can infer entailment
    label = "entailment"

print(label)

