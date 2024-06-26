# Define variables with representative names for the numerical entities in both inputs
john_share = 2
jose_share = 4
binoy_share = 6
total_share = 14

# Extract all quantities as valid numbers (integers or floats)
john_share_num = 2600
jose_share_num = 2600
binoy_share_num = 2600
total_share_num = 6600

# Use brief comments to explain what comparison you do between the defined variables
if john_share_num <= jose_share_num and jose_share_num <= binoy_share_num:
    # Check if the estimate of 'john_share_num' contradicts the number of shares in the premise
    label = "contradiction"
elif john_share_num + jose_share_num + binoy_share_num!= total_share_num:
    # Check if the number of shares in the hypothesis contradicts the total number of shares in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
