# Premise: Yesterday it took Robert more than 1 hours to drive from City X to City Y.
# Hypothesis: Yesterday it took Robert 3 hours to drive from City X to City Y.
# Golden Label: neutral

drive_time_premise = 1
drive_time_hypothesis = 3

# the hypothesis talks about the duration of Robert's drive, referenced also in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time
    # any drive time greater than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
