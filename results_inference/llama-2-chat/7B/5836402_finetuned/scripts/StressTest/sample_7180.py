drive_time_premise_less = 5
drive_time_premise_more = 3
drive_time_hypothesis_less = 1
drive_time_hypothesis_more = 3

drive_speed_premise_less = 42
drive_speed_premise_more = 60
drive_speed_hypothesis_less = 42
drive_speed_hypothesis_more = 60

# the hypothesis refers to the drive time and speed mentioned in the premise
if drive_time_hypothesis_less > drive_time_premise_less or drive_time_hypothesis_more < drive_time_premise_more:
    # check if the hypothesis contradicts the drive time in the premise
    label = "contradiction"
elif drive_speed_hypothesis_less > drive_speed_premise_less or drive_speed_hypothesis_more < drive_speed_premise_more:
    # check if the hypothesis contradicts the drive speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
