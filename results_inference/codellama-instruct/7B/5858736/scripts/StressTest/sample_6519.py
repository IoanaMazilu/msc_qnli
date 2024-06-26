# Define variables for the premise
distance_traveled_premise = 8
average_speed_premise = 40
time_stopped_premise = 14
distance_traveled_2_premise = 20
average_speed_2_premise = 60

# Define variables for the hypothesis
distance_traveled_hypothesis = 5
average_speed_hypothesis = 40
time_stopped_hypothesis = 14
distance_traveled_2_hypothesis = 20
average_speed_2_hypothesis = 60

# Calculate the total time traveled
total_time_premise = distance_traveled_premise / average_speed_premise + time_stopped_premise + distance_traveled_2_premise / average_speed_2_premise
total_time_hypothesis = distance_traveled_hypothesis / average_speed_hypothesis + time_stopped_hypothesis + distance_traveled_2_hypothesis / average_speed_2_hypothesis

# Check if the total time in the hypothesis is greater than the total time in the premise
if total_time_hypothesis > total_time_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
