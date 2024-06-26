# Define the variables
distance_per_trip = 256.0
total_trips = 32.0
total_distance = 8191.0

# Calculate the total distance
total_distance_calculated = distance_per_trip * total_trips

# Check if the hypothesis value matches the calculated value
if total_distance_calculated!= total_distance:
    # If the values don't match, we have a contradiction
    label = "contradiction"
else:
    # If the values match, we have entailment
    label = "entailment"

print(label)
