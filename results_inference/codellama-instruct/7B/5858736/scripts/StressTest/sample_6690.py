# Define variables with representative names for the numerical entities in both inputs
total_journey = 8800
travelled_distance = 1800

# Extract all quantities as valid numbers (integers or floats)
total_journey = int(total_journey)
travelled_distance = int(travelled_distance)

# Use brief comments to explain what comparison you do between the defined variables
if travelled_distance <= total_journey:
    # Check if the estimate of 'travelled_distance' contradicts the total journey
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
