# Define variables for the numerical entities in the premise and hypothesis
premise_fishbowls = 261.0
premise_fish_per_fishbowl = 23.0
hypothesis_fish = 6003.0

# Extract all quantities as valid numbers
total_fishbowls = premise_fishbowls * premise_fish_per_fishbowl
total_fish = total_fishbowls * premise_fish_per_fishbowl

# Use brief comments to explain what comparison you do between the defined variables
if total_fish >= hypothesis_fish:
    # Check if the total number of fish from the hypothesis is greater than or equal to the total number of fish in the premise
    label = "entailment"
else:
    # If the total number of fish from the hypothesis is less than the total number of fish in the premise, we can infer contradiction
    label = "contradiction"

print(label)
