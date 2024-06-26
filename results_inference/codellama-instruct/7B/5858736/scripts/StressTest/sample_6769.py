# Define variables with representative names for the numerical entities in both inputs
john_share = 2600
jose_share = 4000
binoy_share = 6000
total_share = 2 + 4 + 6 = 12

# Extract all quantities as valid numbers (integers or floats)
john_share = 2600
jose_share = 4000
binoy_share = 6000
total_share = 12

# Use brief comments to explain what comparison you do between the defined variables
if john_share + jose_share + binoy_share <= total_share:
    # Check if the sum of the shares of John, Jose and Binoy is greater than or equal to the total share
    label = "contradiction"
else:
    # If the sum of the shares of John, Jose and Binoy is greater than the total share, we can infer entailment
    label = "entailment"

print(label)
