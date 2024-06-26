# Define variables for the premise
distance_premise = 80
walking_speed_premise = 4
running_speed_premise = 6

# Define variables for the hypothesis
distance_hypothesis = 20
walking_speed_hypothesis = 4
running_speed_hypothesis = 6

# Calculate the distance traveled by Maxwell
distance_maxwell = distance_premise * walking_speed_premise

# Calculate the distance traveled by Brad
distance_brad = distance_hypothesis * running_speed_hypothesis

# Check if the distance traveled by Brad contradicts the premise
if distance_brad <= distance_maxwell:
    label = "contradiction"
else:
    label = "entailment"

print(label)
