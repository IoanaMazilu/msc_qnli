# Define variables with representative names for the numerical entities in both inputs
walked_distance_premise = 4.0
walking_speed_premise = 3.0
walked_time_hypothesis = 2.9

# Extract all quantities as valid numbers (integers or floats)
walked_distance_premise = float(walked_distance_premise)
walking_speed_premise = float(walking_speed_premise)
walked_time_hypothesis = float(walked_time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Find the total distance walked from the premise
total_distance_walked_premise = walked_distance_premise * walking_speed_premise

# Check if the total distance walked from the hypothesis contradicts the estimate of more than 'total_distance_walked_premise'
if walked_time_hypothesis * walking_speed_premise >= total_distance_walked_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
