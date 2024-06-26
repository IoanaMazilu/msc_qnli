# Define variables with representative names for the numerical entities in both inputs
demand = 1.5
supply = 1.5

# Extract all quantities as valid numbers (integers or floats)
demand = float(demand)
supply = float(supply)

# Use brief comments to explain what comparison you do between the defined variables
if demand > supply:
    # Check if the demand is greater than the supply
    label = "entailment"
else:
    # Check if the demand is less than or equal to the supply
    label = "contradiction"

print(label)
