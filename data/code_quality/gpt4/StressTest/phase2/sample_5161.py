drive_time_premise = 7
drive_time_hypothesis = 5
drive_speed_premise = 80
drive_speed_hypothesis = 80

# the hypothesis talks about the drive time and speed from Town X to Town Z, referenced also in the premise
if drive_time_hypothesis >= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
elif drive_speed_hypothesis != drive_speed_premise:
    # check if the drive speed in the hypothesis contradicts the drive speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time
    # any drive time less than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
