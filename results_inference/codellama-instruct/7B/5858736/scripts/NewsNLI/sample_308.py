# Define variables with representative names for the numerical entities in both inputs
street_kids_premise = 12000
street_kids_hypothesis = 12000

# Extract all quantities as valid numbers (integers or floats)
# Do not ignore any quantity or numerical information

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if street_kids_hypothesis!= street_kids_premise:
    # Check if the number of street kids in the hypothesis contradicts the number of street kids in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
