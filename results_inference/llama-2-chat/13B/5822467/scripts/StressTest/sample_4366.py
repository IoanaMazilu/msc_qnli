# Define variables with representative names for the numerical entities in both inputs
x_premise = 60
x_hypothesis = 40

# Extract all quantities as valid numbers (integers or floats)
hours_premise = int(x_premise / 2)
hours_hypothesis = int(x_hypothesis / 2)

# Perform calculations if necessary
pay_premise = 2 * hours_premise * x_premise
pay_hypothesis = 2 * hours_hypothesis * x_hypothesis

# Compare the variables
if pay_premise > pay_hypothesis:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif pay_hypothesis > pay_premise:
    # The premise contradicts the hypothesis
    label = "contradiction"
else:
    # The premise and hypothesis are consistent, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
