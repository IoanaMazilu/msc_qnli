# Define variables with representative names for the numerical entities in both inputs
compound_interest_premise = 8
compound_interest_hypothesis = 4

# Extract all quantities as valid numbers (integers or floats)
compound_interest_premise = float(compound_interest_premise)
compound_interest_hypothesis = float(compound_interest_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if compound_interest_hypothesis <= compound_interest_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'compound_interest_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the compound interest earned by Sunil
    # Any number of compound interest greater than 'compound_interest_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
