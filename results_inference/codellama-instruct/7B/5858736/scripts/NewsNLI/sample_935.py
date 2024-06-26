# Define variables with representative names for the numerical entities in both inputs
fatalities_premise = 4
fatalities_hypothesis = 5

# Extract all quantities as valid numbers (integers or floats)
fatalities_premise = int(fatalities_premise)
fatalities_hypothesis = int(fatalities_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if fatalities_hypothesis > fatalities_premise:
    # Check if the number of fatalities in the hypothesis is greater than the number of fatalities in the premise
    label = "entailment"
else:
    # If the number of fatalities in the hypothesis is not greater than the number of fatalities in the premise, we can infer neutrality
    label = "neutral"

print(label)
