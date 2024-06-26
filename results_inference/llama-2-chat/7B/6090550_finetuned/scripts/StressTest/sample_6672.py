drive_time_40_premise = 1
drive_time_60_premise = 3
drive_time_40_hypothesis = 5
drive_time_60_hypothesis = 3

# the hypothesis refers to the drive time and speed mentioned in the premise
if drive_time_40_premise!= drive_time_40_hypothesis:
    # check if the drive time at 40 mph in the hypothesis contradicts the drive time at 40 mph in the premise
    label = "contradiction"
elif drive_time_60_premise!= drive_time_60_hypothesis:
    # check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
