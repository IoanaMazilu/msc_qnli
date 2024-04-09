# Importante: define variables with representative names for the numerical entities in both inputs
microTron_premise = 36
microTron_hypothesis = 76
dynaco_premise = 48
dynaco_hypothesis = 48

# Extract all quantities as valid numbers (integers or floats)
share_premise = 300
share_hypothesis = 300
price_per_share_premise = 40
price_per_share_hypothesis = 40

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)
# For example, if we know "A is more than B", then we can either check if A>B for entailment or if B<=A for contradiction

# Check if the hypothesis value contradicts the premise value
if dynaco_hypothesis <= dynaco_premise:
    label = "contradiction"

# Check if the premise value gives an estimate for the number of shares sold
# and any number of shares greater than that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
else:
    label = "neutral"

# Print the label
print(label)
