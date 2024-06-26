drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis refers to the drive time from City A to City B, which is also mentioned in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the drive time in the premise
    label = "contradiction"
elif drive_time_hypothesis > drive_time_premise:
    # check if the hypothesis value is greater than the drive time in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the drive time in the premise, it is neutral
    label = "neutral"

print(label)
