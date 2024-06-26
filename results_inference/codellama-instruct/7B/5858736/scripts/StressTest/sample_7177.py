# Define variables with representative names for the numerical entities in both inputs
john_share = 2
jose_share = 4
binoy_share = 6
total_share = 14

# Extract all quantities as valid numbers (integers or floats)
john_share_premise = 3800
jose_share_premise = 3800
binoy_share_premise = 3800
total_share_premise = 14000

john_share_hypothesis = 4800
jose_share_hypothesis = 4800
binoy_share_hypothesis = 4800
total_share_hypothesis = 14400

# Use brief comments to explain what comparison you do between the defined variables
if john_share_hypothesis <= john_share_premise:
    # Check if the estimate of 'john_share_hypothesis' contradicts the number of shares in the premise
    label = "contradiction"
elif jose_share_hypothesis <= jose_share_premise:
    # Check if the estimate of 'jose_share_hypothesis' contradicts the number of shares in the premise
    label = "contradiction"
elif binoy_share_hypothesis <= binoy_share_premise:
    # Check if the estimate of 'binoy_share_hypothesis' contradicts the number of shares in the premise
    label = "contradiction"
elif total_share_hypothesis <= total_share_premise:
    # Check if the estimate of 'total_share_hypothesis' contradicts the number of shares in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
