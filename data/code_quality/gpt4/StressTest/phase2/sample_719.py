drive_time_premise = 3
drive_time_hypothesis = 8

# the hypothesis talks about the same driving time from City X to City Y as the premise
if drive_time_premise == drive_time_hypothesis:
    # check if the drive time in the hypothesis is the same as the one mentioned in the premise
    label = "entailment"
elif drive_time_hypothesis < drive_time_premise:
    # check if the drive time in the hypothesis contradicts the drive time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific driving time
    # any driving time longer than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
