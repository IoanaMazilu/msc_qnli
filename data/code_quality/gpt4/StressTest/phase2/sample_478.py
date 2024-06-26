drive_hours_premise = 4
drive_hours_hypothesis = 8
drive_rate_premise = 40
drive_rate_hypothesis = 40

# the hypothesis talks about the drive duration and rate, both mentioned in the premise
if drive_hours_hypothesis <= drive_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'drive_hours_premise'
    label = "contradiction"
elif drive_rate_hypothesis != drive_rate_premise:
    # check if the drive rate in the hypothesis contradicts the drive rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive duration
    # any drive duration greater than 'drive_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
