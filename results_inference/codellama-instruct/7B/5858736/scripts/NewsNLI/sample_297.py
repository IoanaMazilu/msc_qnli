# Define variables with representative names for the numerical entities in both inputs
num_people_premise = 20
num_people_hypothesis = 30

# Extract all quantities as valid numbers (integers or floats)
num_people_premise = int(num_people_premise)
num_people_hypothesis = int(num_people_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_people_hypothesis > num_people_premise:
    # Check if the number of people thought trapped in the casino because of debris exceeds the number of people trapped in the casino
    label = "entailment"
else:
    # If the number of people thought trapped in the casino because of debris does not exceed the number of people trapped in the casino, we can infer neutrality
    label = "neutral"

print(label)
