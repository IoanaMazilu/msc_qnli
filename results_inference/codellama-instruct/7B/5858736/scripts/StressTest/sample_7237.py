# Define variables with representative names for the numerical entities in both inputs
distance_traveled_premise = 440
distance_traveled_hypothesis = 240

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis value contradicts the estimate of less than 'distance_traveled_premise'
if distance_traveled_hypothesis >= distance_traveled_premise:
    label = "contradiction"
else:
    # Any number of miles greater than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
