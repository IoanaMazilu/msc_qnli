# Define variables with representative names for the numerical entities in both inputs
business_value_premise = 64000
business_value_hypothesis = 14000

# Extract all quantities as valid numbers (integers or floats)
business_value_premise = int(business_value_premise)
business_value_hypothesis = int(business_value_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if business_value_hypothesis <= business_value_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'business_value_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the business value
    # Any number of business value greater than 'business_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
