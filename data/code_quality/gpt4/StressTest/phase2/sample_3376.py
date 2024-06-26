drive_time_premise = 8
drive_time_hypothesis = 3

# the hypothesis talks about the time Robert took to drive from City A to City B, which is also referenced in the premise
if drive_time_hypothesis >= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time
    # any driving time less than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
