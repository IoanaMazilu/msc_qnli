# Define variables with representative names for the numerical entities in both inputs
total_journey = 8800
travelled_by_air = 1800

# Extract all quantities as valid numbers (integers or floats)
total_journey = float(total_journey)
travelled_by_air = float(travelled_by_air)

# Use brief comments to explain what comparison you do between the defined variables
if travelled_by_air <= total_journey:
    # Check if the estimate of 'travelled_by_air' contradicts the total journey
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
