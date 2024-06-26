# Define variables with representative names for the numerical entities in both inputs
cost_price = 100
selling_price = 92

# Extract all quantities as valid numbers (integers or floats)
cost_price = float(cost_price)
selling_price = float(selling_price)

# Use brief comments to explain what comparison you do between the defined variables
if selling_price <= cost_price * 0.88:
    # Check if the estimate of'selling_price' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
