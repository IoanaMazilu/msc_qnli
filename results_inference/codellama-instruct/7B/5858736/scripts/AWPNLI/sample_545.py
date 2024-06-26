# Define variables with representative names for the numerical entities in both inputs
mrs_sheridan_cats_premise = 17.0
mrs_sheridan_cats_given_away_premise = 14.0
sheridan_cats_hypothesis = 5.0

# Extract all quantities as valid numbers (integers or floats)
total_cats_premise = mrs_sheridan_cats_premise - mrs_sheridan_cats_given_away_premise

# Use brief comments to explain what comparison you do between the defined variables
# Check if the total number of cats from the hypothesis contradicts the estimate of more than'mrs_sheridan_cats_given_away_premise'
if total_cats_premise > sheridan_cats_hypothesis:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
