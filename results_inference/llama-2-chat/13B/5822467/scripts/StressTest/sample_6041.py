# Define variables with representative names for the numerical entities in both inputs
speed_premise = 90
time_increase_premise = 12
speed_hypothesis = float(input("Enter the speed of Xavier: "))

# Extract all quantities as valid numbers (integers or floats)
if speed_hypothesis > speed_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # Check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # Check if the hypothesis value entails the premise value
    label = "entailment"

# Use brief comments to explain what comparison you do between the defined variables
# Refrain from concluding in the comments the entailment/contradiction or neutral relation
print(label)
