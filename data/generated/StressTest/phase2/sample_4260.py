# Premise: Frank is 15 years younger then John.
# Hypothesis: Frank is less than 25 years younger then John.
# Golden Label: entailment

age_diff_premise = 15
age_diff_hypothesis = 25

# the hypothesis discusses the age difference between Frank and John, also referenced in the premise
if age_diff_hypothesis < age_diff_premise:
    # check if the hypothesis value contradicts the age difference stated in the premise
    label = "contradiction"
elif age_diff_hypothesis == age_diff_premise:
    # if the hypothesis exactly matches the premise, we can infer entailment
    label = "entailment"
else:
    # the hypothesis gives an estimate for the age difference that is larger than the one in the premise
    # any age difference less than 'age_diff_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

