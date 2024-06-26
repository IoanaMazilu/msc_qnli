first_drive_distance_premise = 340
first_drive_speed_premise = 60
second_drive_distance_premise = 120
second_drive_speed_premise = 40

first_drive_distance_hypothesis = 240
first_drive_speed_hypothesis = 60
second_drive_distance_hypothesis = 120
second_drive_speed_hypothesis = 40

# the hypothesis refers to the distances and speeds of Joe's drives mentioned in the premise
if first_drive_distance_hypothesis > first_drive_distance_premise:
    # check if the distance of the first drive in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif first_drive_speed_hypothesis!= first_drive_speed_premise or second_drive_distance_hypothesis!= second_drive_distance_premise or second_drive_speed_hypothesis!= second_drive_speed_premise:
    # check if the speed or distances of the drives in the hypothesis contradict the speeds or distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
