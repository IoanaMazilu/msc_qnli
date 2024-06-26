# Define variables for the premise
distance_home_premise = 20
walking_speed_premise = 4
running_speed_premise = 6

# Define variables for the hypothesis
distance_home_hypothesis = 80
walking_speed_hypothesis = 4
running_speed_hypothesis = 6

# Calculate the distance traveled by Maxwell
distance_traveled_maxwell = distance_home_premise * walking_speed_premise

# Calculate the distance traveled by Brad
distance_traveled_brad = distance_home_hypothesis * running_speed_hypothesis

# Check if the distance traveled by Brad contradicts the premise
if distance_traveled_brad > distance_traveled_maxwell:
    label = "contradiction"
else:
    # If the distance traveled by Brad does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
