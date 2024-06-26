# Define variables for the premise and hypothesis
units_digits_premise = 8
units_digits_hypothesis = 7

# Check if the hypothesis value is greater than the premise value
if units_digits_hypothesis > units_digits_premise:
    # The hypothesis value is greater than the premise value, so the hypothesis is entailed
    label = "entailment"
else:
    # The hypothesis value is less than or equal to the premise value, so the hypothesis is not entailed
    label = "contradiction"

print(label)
