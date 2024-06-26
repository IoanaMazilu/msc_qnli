drive_time_premise = 1 * 60 = 60
drive_time_hypothesis = 3 * 60 = 180

# the hypothesis talks about the total drive time, which is estimated in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of total drive time in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the total drive time, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
