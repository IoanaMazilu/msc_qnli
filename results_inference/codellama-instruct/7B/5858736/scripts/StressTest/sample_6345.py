# Define variables with representative names for the numerical entities in both inputs
business_investment_premise = 50000
business_investment_hypothesis = 10000

# Extract all quantities as valid numbers (integers or floats)
business_investment_premise = int(business_investment_premise)
business_investment_hypothesis = int(business_investment_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if business_investment_hypothesis <= business_investment_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise, so the hypothesis is entailed
    label = "entailment"

print(label)