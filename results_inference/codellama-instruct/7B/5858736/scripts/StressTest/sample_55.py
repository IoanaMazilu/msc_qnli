# Define variables with representative names for the numerical entities in both inputs
speed_Bruce_premise = 60
speed_Bhishma_premise = 20
speed_Bruce_hypothesis = 30
speed_Bhishma_hypothesis = 20

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis values contradict the premise ones
if speed_Bruce_hypothesis > speed_Bruce_premise:
    label = "contradiction"
elif speed_Bhishma_hypothesis!= speed_Bhishma_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
