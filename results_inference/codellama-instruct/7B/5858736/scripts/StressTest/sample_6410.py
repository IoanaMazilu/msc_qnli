# Define variables for the numerical entities in the premise and hypothesis
shirt_price_premise = 20
shirt_price_hypothesis = 80

# Extract the quantities as valid numbers
shirt_price_premise = float(shirt_price_premise)
shirt_price_hypothesis = float(shirt_price_hypothesis)

# Use brief comments to explain the comparison
if shirt_price_hypothesis <= shirt_price_premise:
    # Check if the hypothesis value contradicts the estimate of 20% off for every shirt
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
