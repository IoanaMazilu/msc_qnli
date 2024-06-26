# Define variables with representative names for the numerical entities in both inputs
fish_premise = 261.0
fish_per_fishbowl_premise = 23.0
fishbowls_hypothesis = 12.5

# Extract all quantities as valid numbers
total_fish_premise = fish_premise * fish_per_fishbowl_premise
total_fishbowls_hypothesis = fishbowls_hypothesis

# Use brief comments to explain what comparison you do between the defined variables
if total_fish_premise >= total_fishbowls_hypothesis:
    # Check if the total number of fish from the premise is greater than or equal to the number of fishbowls in the hypothesis
    label = "entailment"
else:
    # If the total number of fish from the premise is less than the number of fishbowls in the hypothesis, we can infer contradiction
    label = "contradiction"

print(label)
