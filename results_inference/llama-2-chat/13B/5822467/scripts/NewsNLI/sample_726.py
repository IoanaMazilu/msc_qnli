# Define variables with representative names for the numerical entities in both inputs
deaths_premise = 3
deaths_hypothesis = 32

# Extract all quantities as valid numbers (integers or floats)
deaths_premise_int = int(deaths_premise)
deaths_hypothesis_int = int(deaths_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Refrain from concluding in the comments the entailment/contradiction or neutral relation

# Use the variables to perform calculations if necessary
# Finally compare them accordingly to infer one of the following labels

# If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
if deaths_hypothesis_int == deaths_premise_int:
    # Infer entailment
    label = "entailment"

# If the hypothesis values contradict the premise values, we can infer contradiction
elif deaths_hypothesis_int!= deaths_premise_int:
    # Infer contradiction
    label = "contradiction"

# If the hypothesis values do not contradict the premise values, we can infer neutrality
else:
    # Infer neutrality
    label = "neutral"

# Print the label
print(label)
