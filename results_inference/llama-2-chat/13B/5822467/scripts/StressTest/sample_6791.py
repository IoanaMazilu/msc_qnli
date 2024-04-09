# Define variables with representative names for the numerical entities in both inputs
maxwell_walking_speed = 4
brad_running_speed = 6
distance_premise = 50

# Extract all quantities as valid numbers (integers or floats)
distance_hypothesis = float(input("Enter the distance between their homes: "))

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)

# Check if the hypothesis value contradicts the estimate of the distance in the premise
if distance_hypothesis > distance_premise:
    # The hypothesis value contradicts the estimate of the distance in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # The hypothesis value is consistent with the estimate of the distance in the premise
    label = "neutral"
else:
    # The hypothesis value is greater than the estimate of the distance in the premise
    label = "entailment"

print(label)
