# Define variables with representative names for the numerical entities in both inputs
earmuffs_premise = 6444.0
earmuffs_hypothesis = 5100.0

# Extract all quantities as valid numbers (integers or floats)
less_earmuffs_premise = 1346.0

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the total number of earmuffs sold in the premise and hypothesis
if earmuffs_hypothesis > earmuffs_premise:
    # Check if the total number of earmuffs in the hypothesis contradicts the premise
    label = "contradiction"
elif earmuffs_hypothesis < earmuffs_premise:
    # Check if the total number of earmuffs in the hypothesis entails the premise
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
