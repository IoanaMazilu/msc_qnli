first_leg_distance_premise = 600
first_leg_speed_premise = 60
second_leg_distance_premise = 120
second_leg_speed_premise = 40

first_leg_distance_hypothesis = 100
first_leg_speed_hypothesis = 60
second_leg_distance_hypothesis = 120
second_leg_speed_hypothesis = 40

# checking if the distance and speed of the first leg of the drive in the hypothesis contradicts the premise
if first_leg_distance_hypothesis != first_leg_distance_premise or first_leg_speed_hypothesis != first_leg_speed_premise:
    label = "contradiction"
# checking if the distance and speed of the second leg of the drive in the hypothesis contradicts the premise
elif second_leg_distance_hypothesis != second_leg_distance_premise or second_leg_speed_hypothesis != second_leg_speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
