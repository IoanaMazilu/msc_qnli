# Define variables with representative names for the numerical entities in both inputs
rahul_age_premise = 26
deepak_age_premise = 26
rahul_deepak_ratio_premise = 4/3

# Extract all quantities as valid numbers (integers or floats)
rahul_age_hypothesis = 26
deepak_age_hypothesis = 26
rahul_deepak_ratio_hypothesis = 1/3

# Use brief comments to explain what comparison you do between the defined variables
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'rahul_deepak_ratio_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio between Rahul and Deepak
    # Any ratio greater than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
