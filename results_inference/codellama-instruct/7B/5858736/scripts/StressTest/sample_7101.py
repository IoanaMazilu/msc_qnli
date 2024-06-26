# Define variables for the numerical entities in both inputs
distance_driven_premise = 240
speed_premise = 60
distance_driven_hypothesis = 120
speed_hypothesis = 40

# Extract all quantities as valid numbers
distance_driven_premise = float(distance_driven_premise)
speed_premise = float(speed_premise)
distance_driven_hypothesis = float(distance_driven_hypothesis)
speed_hypothesis = float(speed_hypothesis)

# Calculate the total distance driven
total_distance_driven_premise = distance_driven_premise + (speed_premise * 60)
total_distance_driven_hypothesis = distance_driven_hypothesis + (speed_hypothesis * 60)

# Compare the total distance driven
if total_distance_driven_hypothesis <= total_distance_driven_premise:
    # Check if the estimate of 'total_distance_driven_hypothesis' contradicts the total distance driven in the premise
    label = "contradiction"
else:
    # The hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
