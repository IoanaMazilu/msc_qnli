# Define variables with representative names for the numerical entities in both inputs
maxwell_walking_speed = 4
brad_running_speed = 6
distance_premise = 20

# Extract all quantities as valid numbers (integers or floats)
distance_hypothesis = float(input("Enter the distance between their homes: "))

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the distance in the hypothesis to the distance in the premise
if distance_hypothesis < distance_premise:
    # Check if the hypothesis value contradicts the estimate of the distance in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # Check if the hypothesis value entails the estimate of the distance in the premise
    label = "entailment"
else:
    # If the hypothesis value is equal to the distance in the premise, there is no contradiction or entailment
    label = "neutral"

print(label)
