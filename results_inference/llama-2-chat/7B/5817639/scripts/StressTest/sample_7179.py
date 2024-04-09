drive_time_premise = 1 + 3 = 4
drive_speed_premise = 42
drive_speed_hypothesis = 60

# the hypothesis talks about the drive time and speed, referenced also in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of 'drive_time_premise'
    label = "contradiction"
elif drive_speed_hypothesis!= drive_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'drive_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
