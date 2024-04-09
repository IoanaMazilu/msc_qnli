# Define variables with representative names for the numerical entities in both inputs
sheep_premise = 6
horses_premise = 7
food_per_horse = 230
total_food_needed = 12880

# Extract all quantities as valid numbers (integers or floats)
sheep_hypothesis = float(input("Enter the number of sheep in the farm: "))
horses_hypothesis = float(input("Enter the number of horses in the farm: "))

# Perform calculations if necessary
if sheep_hypothesis < horses_hypothesis:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif sheep_hypothesis > horses_hypothesis:
    # Check if the hypothesis value entails the premise
    label = "entailment"
else:
    # Check if the hypothesis value is neutral with respect to the premise
    label = "neutral"

print(label)
