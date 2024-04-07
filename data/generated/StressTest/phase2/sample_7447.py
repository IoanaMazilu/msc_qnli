# Premise: Ratio between Rahul and Deepak is more than 1:3, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 26 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 1/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# The hypothesis provides specific values for the ratio between Rahul and Deepak's ages and Rahul's future age
# These are also referenced in the premise
if rahul_future_age_hypothesis != rahul_future_age_premise:
    # Check if the predicted future age for Rahul in the hypothesis contradicts the predicted future age in the premise
    label = "contradiction"
elif rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # Check if the ratio between Rahul and Deepak's ages in the hypothesis contradicts the estimate of more than 'rahul_deepak_ratio_premise'
    label = "contradiction"
else:
    # The premise provides an estimate for the ratio between Rahul and Deepak's ages
    # Any ratio greater than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

