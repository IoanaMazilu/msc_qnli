drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis talks about a shorter drive time than the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time
    # any drive time shorter than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
