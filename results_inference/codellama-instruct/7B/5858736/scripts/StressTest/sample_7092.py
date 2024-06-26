# Define variables for the numerical entities in the premise and hypothesis
rahul_age_premise = 26
deepak_age_premise = 26
rahul_deepak_ratio_premise = 5/2

# Extract all quantities as valid numbers
rahul_age_hypothesis = 26
deepak_age_hypothesis = 26
rahul_deepak_ratio_hypothesis = 8/2

# Check if the ratio in the hypothesis contradicts the ratio in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # The hypothesis value contradicts the estimate of more than 'rahul_deepak_ratio_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio
    # Any number of years greater than 'rahul_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
