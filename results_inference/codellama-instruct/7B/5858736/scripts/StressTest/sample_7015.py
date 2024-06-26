# Define variables for the premise and hypothesis
age_ratio_premise = 6/2
age_ratio_hypothesis = 1/2

# Check if the hypothesis value contradicts the premise
if age_ratio_hypothesis > age_ratio_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
