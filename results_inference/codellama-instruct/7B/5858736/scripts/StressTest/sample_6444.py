# Define variables with representative names for the numerical entities in both inputs
age_frank_premise = 14
age_john_premise = 84
age_frank_hypothesis = 84

# Extract all quantities as valid numbers (integers or floats)
age_frank_premise = int(age_frank_premise)
age_john_premise = int(age_john_premise)
age_frank_hypothesis = int(age_frank_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if age_frank_hypothesis <= (age_john_premise - age_frank_premise):
    # Check if the estimate of 'age_frank_hypothesis' contradicts the difference between the ages of Frank and John in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
