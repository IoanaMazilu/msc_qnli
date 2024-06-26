# Define variables with representative names for the numerical entities in both inputs
age_premise = 23
age_hypothesis = 23

# Extract all quantities as valid numbers (integers or floats)
age_premise = int(age_premise)
age_hypothesis = int(age_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if age_hypothesis!= age_premise:
    # Check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
