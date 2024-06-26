# Define variables with representative names for the numerical entities in both inputs
people_injured_premise = 100
people_injured_hypothesis = 2

# Extract all quantities as valid numbers (integers or floats)
people_injured_premise = int(people_injured_premise)
people_injured_hypothesis = int(people_injured_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if people_injured_hypothesis > people_injured_premise:
    # Check if the number of people being treated for serious injuries in the hypothesis exceeds the number of people being treated for minor injuries in the premise
    label = "entailment"
else:
    # If the number of people being treated for serious injuries in the hypothesis does not exceed the number of people being treated for minor injuries in the premise, we can infer neutrality
    label = "neutral"

print(label)
