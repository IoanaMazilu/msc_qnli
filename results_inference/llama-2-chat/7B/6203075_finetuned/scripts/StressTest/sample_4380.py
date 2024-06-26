drive_time_premise = 1 + 3
drive_time_hypothesis = 8
drive_speed_premise = 50
drive_speed_hypothesis = 50

# the hypothesis refers to the drive time and speed mentioned in the premise
if drive_time_premise <= drive_time_hypothesis:
    # check if the estimate of 'drive_time_hypothesis' contradicts the drive time in the premise
    label = "contradiction"
elif drive_speed_premise!= drive_speed_hypothesis:
    # check if the estimate of 'drive_speed_hypothesis' contradicts the drive speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
