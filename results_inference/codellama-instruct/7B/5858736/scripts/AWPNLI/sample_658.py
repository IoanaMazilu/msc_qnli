# Define variables with representative names for the numerical entities in both inputs
points_per_round_hypothesis = 7.0
games_played_premise = 3
total_points_premise = 21

# Extract all quantities as valid numbers
total_points_hypothesis = points_per_round_hypothesis * games_played_premise

# Use brief comments to explain what comparison you do between the defined variables
if total_points_hypothesis >= total_points_premise:
    # Check if the total points from the hypothesis are greater than or equal to the total points in the premise
    label = "entailment"
else:
    # If the total points from the hypothesis are less than the total points in the premise, we can infer contradiction
    label = "contradiction"

print(label)
