# Define variables for the premise and hypothesis
age_ratio_premise = 7/3
age_ratio_hypothesis = 1/3

# Check if the hypothesis value contradicts the premise value
if age_ratio_hypothesis!= age_ratio_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise value, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
