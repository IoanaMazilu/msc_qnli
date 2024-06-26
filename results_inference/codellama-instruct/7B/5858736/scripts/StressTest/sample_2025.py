# Define variables with representative names for the numerical entities in both inputs
age_john_premise = 6
age_tom_premise = 6
age_john_hypothesis = 5

# Extract all quantities as valid numbers (integers or floats)
age_john_premise = int(age_john_premise)
age_tom_premise = int(age_tom_premise)
age_john_hypothesis = int(age_john_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if age_john_hypothesis <= age_john_premise:
    # Check if the estimate of 'age_john_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
