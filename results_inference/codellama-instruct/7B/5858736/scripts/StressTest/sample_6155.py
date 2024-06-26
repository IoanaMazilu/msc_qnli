# Define variables with representative names for the numerical entities in both inputs
age_john_premise = 21
age_wilson_premise = 21
age_john_hypothesis = 71
age_wilson_hypothesis = 71

# Extract all quantities as valid numbers (integers or floats)
age_john_premise = int(age_john_premise)
age_wilson_premise = int(age_wilson_premise)
age_john_hypothesis = int(age_john_hypothesis)
age_wilson_hypothesis = int(age_wilson_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if age_john_hypothesis <= age_john_premise * 2:
    # Check if the estimate of 'age_john_hypothesis' contradicts the number of years John will be twice as old as Wilson
    label = "contradiction"
elif age_wilson_hypothesis!= age_wilson_premise:
    # Check if the number of years Wilson will be in the hypothesis contradicts the number of years Wilson will be in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
