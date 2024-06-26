# Define variables for the premise
distance_traveled_premise = 8
average_speed_premise = 40
time_stopped_premise = 11
distance_traveled_2_premise = 20
average_speed_2_premise = 60

# Define variables for the hypothesis
distance_traveled_hypothesis = 4
average_speed_hypothesis = 40
time_stopped_hypothesis = 11
distance_traveled_2_hypothesis = 20
average_speed_2_hypothesis = 60

# Check if the hypothesis values contradict the premise
if distance_traveled_hypothesis <= distance_traveled_premise:
    label = "contradiction"
elif average_speed_hypothesis!= average_speed_premise:
    label = "contradiction"
elif time_stopped_hypothesis!= time_stopped_premise:
    label = "contradiction"
elif distance_traveled_2_hypothesis <= distance_traveled_2_premise:
    label = "contradiction"
elif average_speed_2_hypothesis!= average_speed_2_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
