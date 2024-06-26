# Define variables with representative names for the numerical entities in both inputs
original_investment = 3
years = 1

# Extract all quantities as valid numbers (integers or floats)
original_investment = float(original_investment)
years = int(years)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if years > 0:
    # Check if the hypothesis value contradicts the premise
    if Sandy_got_back_hypothesis <= original_investment * 2:
        label = "contradiction"
    else:
        # If the hypothesis value does not contradict the premise, we can infer entailment
        label = "entailment"
else:
    # If the number of years is negative, the hypothesis is not consistent with the premise
    label = "contradiction"

print(label)
