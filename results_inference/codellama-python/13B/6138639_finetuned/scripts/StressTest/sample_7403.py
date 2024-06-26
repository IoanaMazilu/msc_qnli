drive_time_1_premise = 1
drive_time_1_hypothesis = 3
drive_speed_1_premise = 46
drive_speed_1_hypothesis = 46
drive_time_2_premise = 3
drive_time_2_hypothesis = 3
drive_speed_2_premise = 60
drive_speed_2_hypothesis = 60

# the hypothesis refers to the driving time and speed mentioned in the premise
if drive_time_1_premise!= drive_time_1_hypothesis:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif drive_speed_1_premise!= drive_speed_1_hypothesis:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
elif drive_time_2_premise!= drive_time_2_hypothesis:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif drive_speed_2_premise!= drive_speed_2_hypothesis:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
