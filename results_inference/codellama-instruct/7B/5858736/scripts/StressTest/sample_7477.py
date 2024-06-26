# Define variables for the premise and hypothesis
units_digits_premise = 7
units_digits_hypothesis = 8

# Extract the quantities as valid numbers
units_digits_premise = int(units_digits_premise)
units_digits_hypothesis = int(units_digits_hypothesis)

# Perform the comparison
if units_digits_hypothesis <= units_digits_premise:
    # The hypothesis value contradicts the premise
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise, so the hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
