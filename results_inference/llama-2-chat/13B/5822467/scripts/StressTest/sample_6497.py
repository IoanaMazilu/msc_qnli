# Define variables with representative names for the numerical entities in both inputs
bus_speed_premise = 50
bus_distance_premise = 160 # Mumbai to Pune is approximately 160 km
bus_time_premise = 44

# Define variables with representative names for the numerical entities in the hypothesis
bus_speed_hypothesis = 50
bus_distance_hypothesis = 160
bus_time_hypothesis = 14

# Extract all quantities as valid numbers (integers or floats)
bus_speed_premise = float(bus_speed_premise)
bus_distance_premise = float(bus_distance_premise)
bus_time_premise = float(bus_time_premise)
bus_speed_hypothesis = float(bus_speed_hypothesis)
bus_distance_hypothesis = float(bus_distance_hypothesis)
bus_time_hypothesis = float(bus_time_hypothesis)

# Perform calculations if necessary
bus_time_hypothesis = bus_time_hypothesis / bus_speed_hypothesis # convert time to distance

# Compare the variables
if bus_time_premise > bus_time_hypothesis:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif bus_time_hypothesis > bus_time_premise:
    # The premise contradicts the hypothesis
    label = "contradiction"
elif bus_distance_premise!= bus_distance_hypothesis:
    # The number of bus distance in the hypothesis contradicts the number of bus distance reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
