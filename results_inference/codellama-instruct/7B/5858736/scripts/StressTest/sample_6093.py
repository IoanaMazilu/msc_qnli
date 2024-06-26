# Define variables for the premise and hypothesis
units_digits_premise = 9
units_digits_hypothesis = 8

# Check if the hypothesis value contradicts the premise
if units_digits_hypothesis > units_digits_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
