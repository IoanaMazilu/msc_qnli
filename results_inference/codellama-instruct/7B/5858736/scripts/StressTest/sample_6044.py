# Define variables for the premise
distance_home_premise = 40
walking_speed_premise = 4
running_speed_premise = 6

# Define variables for the hypothesis
distance_home_hypothesis = 80
walking_speed_hypothesis = 4
running_speed_hypothesis = 6

# Calculate the distance traveled by Maxwell
distance_traveled_maxwell = distance_home_hypothesis * walking_speed_hypothesis

# Calculate the distance traveled by Brad
distance_traveled_brad = distance_home_hypothesis * running_speed_hypothesis

# Check if the hypothesis values contradict the premise
if distance_traveled_maxwell <= distance_traveled_brad:
    label = "contradiction"
elif distance_traveled_brad!= distance_traveled_maxwell:
    label = "contradiction"
else:
    label = "entailment"

print(label)
