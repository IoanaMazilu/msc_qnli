# Define variables with representative names for the numerical entities in both inputs
business_investment_premise = 10000
business_investment_hypothesis = 50000

# Extract all quantities as valid numbers (integers or floats)
business_investment_premise = float(business_investment_premise)
business_investment_hypothesis = float(business_investment_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if business_investment_hypothesis <= business_investment_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'business_investment_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of roses
    # Any number of roses greater than 'business_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
