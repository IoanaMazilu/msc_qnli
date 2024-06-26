drive_time_premise = 1
drive_time_hypothesis = 2
speed_premise = 44
speed_hypothesis = 60

# the hypothesis talks about the total drive time and speed, referenced also in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the total drive time, but the hypothesis value is consistent with it
    label = "neutral"

print(label)
