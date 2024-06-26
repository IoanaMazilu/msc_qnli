# Define variables for the numerical entities in the premise and hypothesis
blocks_randy_premise = 78.0
blocks_anna_premise = 19.0
blocks_randy_hypothesis = 102.0

# Extract all quantities as valid numbers
total_blocks_premise = blocks_randy_premise + blocks_anna_premise

# Use brief comments to explain what comparison you do between the defined variables
if total_blocks_hypothesis >= total_blocks_premise:
    # Check if the total blocks from the hypothesis is greater than or equal to the total blocks from the premise
    label = "entailment"
else:
    # If the total blocks from the hypothesis is less than the total blocks from the premise, we can infer contradiction
    label = "contradiction"

print(label)
