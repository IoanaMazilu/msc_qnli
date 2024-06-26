drive_time_premise = 1
drive_time_hypothesis = 1
speed_premise = 44
speed_hypothesis = 44
drive_time_hypothesis_premise = 3
drive_time_hypothesis_speed_premise = 60
drive_time_hypothesis_speed_hypothesis = 60

# the hypothesis refers to the drive time and speed mentioned in the premise
if drive_time_premise!= drive_time_hypothesis:
    # check if the drive time in the hypothesis contradicts the drive time in the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif drive_time_hypothesis_premise!= drive_time_hypothesis or drive_time_hypothesis_speed_premise!= drive_time_hypothesis_speed_hypothesis:
    # check if the drive time or speed in the hypothesis contradicts the drive time or speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
