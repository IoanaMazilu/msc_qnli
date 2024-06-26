# Define variables with representative names for the numerical entities in both inputs
oranges_premise = 45.0
oranges_per_bag_premise = 23.0
bags_hypothesis = 1.4

# Extract all quantities as valid numbers (integers or floats)
total_oranges_premise = oranges_premise * oranges_per_bag_premise

# Use brief comments to explain what comparison you do between the defined variables
if bags_hypothesis * oranges_per_bag_premise == total_oranges_premise:
    # Check if the total number of oranges in the hypothesis is equal to the total number of oranges in the premise
    label = "entailment"
else:
    # If the total number of oranges in the hypothesis is not equal to the total number of oranges in the premise, we can infer contradiction
    label = "contradiction"

print(label)
