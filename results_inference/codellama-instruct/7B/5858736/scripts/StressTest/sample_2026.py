# Define variables with representative names for the numerical entities in both inputs
age_john_premise = 3
age_tom_premise = 1
age_john_hypothesis = 3
age_tom_hypothesis = 1
time_premise = 5
time_hypothesis = 6

# Extract all quantities as valid numbers (integers or floats)
age_john_premise = int(age_john_premise)
age_tom_premise = int(age_tom_premise)
age_john_hypothesis = int(age_john_hypothesis)
age_tom_hypothesis = int(age_tom_hypothesis)
time_premise = int(time_premise)
time_hypothesis = int(time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if age_john_hypothesis * time_hypothesis == age_john_premise * time_premise:
    # Check if the hypothesis value contradicts the estimate of 'age_john_premise'
    label = "contradiction"
elif age_tom_hypothesis * time_hypothesis == age_tom_premise * time_premise:
    # Check if the hypothesis value contradicts the estimate of 'age_tom_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
