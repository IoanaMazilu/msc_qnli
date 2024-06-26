# Define variables for the premise and hypothesis
age_ratio_premise = 5/4
age_ratio_hypothesis = 1/4

# Check if the hypothesis value contradicts the premise value
if age_ratio_hypothesis <= age_ratio_premise:
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise value, so the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
