# Define variables with representative names for the numerical entities in both inputs
miles_trip_premise = 256.0
times_trip_premise = 32.0
miles_hypothesis = 8191.0

# Extract all quantities as valid numbers (integers or floats)
total_miles_premise = miles_trip_premise * times_trip_premise

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if total_miles_premise == miles_hypothesis:
    # Check if the total miles from the hypothesis is equal to the estimate of 8191.0
    label = "entailment"
else:
    # If the hypothesis values and estimates do not equal the premise values, we can infer contradiction
    label = "contradiction"

print(label)
