# Define variables with representative names for the numerical entities in both inputs
fresh_fruit_premise = 9792.0
frozen_fruit_premise = 3513.0
fresh_fruit_hypothesis = 6280.0

# Extract all quantities as valid numbers (integers or floats)
fresh_fruit_premise_int = int(fresh_fruit_premise)
frozen_fruit_premise_int = int(frozen_fruit_premise)
fresh_fruit_hypothesis_int = int(fresh_fruit_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)

# Compare the total amount of fresh fruit sold in the premise and hypothesis
if fresh_fruit_hypothesis_int > fresh_fruit_premise_int:
    # Check if the hypothesis value is greater than the premise value
    label = "entailment"
elif fresh_fruit_hypothesis_int < fresh_fruit_premise_int:
    # Check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # If the hypothesis value is equal to the premise value, no comparison can be made
    label = "neutral"

# Print the label
print(label)
