drive_time_high_speed_premise = 2
drive_time_high_speed_hypothesis = 1
drive_time_low_speed_premise = 3
drive_time_low_speed_hypothesis = 3

# the hypothesis refers to the driving hours at certain speeds from the premise
if drive_time_high_speed_hypothesis > drive_time_high_speed_premise:
    # check if the time driven at high speed in the hypothesis contradicts the time driven at high speed in the premise
    label = "contradiction"
elif drive_time_low_speed_hypothesis != drive_time_low_speed_premise:
    # check if the time driven at low speed in the hypothesis contradicts the time driven at low speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
