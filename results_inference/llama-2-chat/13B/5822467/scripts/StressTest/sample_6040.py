# Define variables with representative names for the numerical entities in both inputs
speed_premise = 10
speed_hypothesis = 90
time_interval_premise = 12
time_interval_hypothesis = 12

# Extract all quantities as valid numbers (integers or floats)
speed_premise = int(speed_premise)
speed_hypothesis = int(speed_hypothesis)
time_interval_premise = int(time_interval_premise)
time_interval_hypothesis = int(time_interval_hypothesis)

# Perform calculations if necessary
time_traveled_premise = speed_premise * time_interval_premise
time_traveled_hypothesis = speed_hypothesis * time_interval_hypothesis

# Compare the variables and infer the label
if speed_hypothesis <= speed_premise:
    # Check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
elif time_traveled_hypothesis!= time_traveled_premise:
    # Check if the time traveled in the hypothesis contradicts the time traveled reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
