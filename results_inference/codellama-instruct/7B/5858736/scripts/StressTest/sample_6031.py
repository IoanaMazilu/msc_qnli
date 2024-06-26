# Define variables with representative names for the numerical entities in both inputs
total_distance = 8/2
traveled_distance = 1/2

# Extract all quantities as valid numbers (integers or floats)
total_distance = float(total_distance)
traveled_distance = float(traveled_distance)

# Use brief comments to explain what comparison you do between the defined variables
if traveled_distance <= total_distance:
    # Check if the estimate of 'traveled_distance' contradicts the total distance reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
