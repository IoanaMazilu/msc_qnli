# Define variables with representative names for the numerical entities in both inputs
maxwell_walking_speed = 4
brad_running_speed = 6
distance_premise = 20

# Extract all quantities as valid numbers
distance_hypothesis = float(input("Enter the distance between their homes: "))

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Check if the distance traveled by Brad can be explicitly entailed from the premise
if distance_hypothesis > distance_premise:
    # The hypothesis contradicts the premise, as Brad cannot walk or run more than the distance stated in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # The hypothesis is neutral, as the distance traveled by Brad is the same as the distance stated in the premise
    label = "neutral"
else:
    # The hypothesis entails the premise, as Brad can walk or run a distance greater than the distance stated in the premise
    label = "entailment"

# Print the label
print(label)
