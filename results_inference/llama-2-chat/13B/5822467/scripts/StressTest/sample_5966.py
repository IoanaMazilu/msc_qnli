robert_drive_premise = 4
robert_drive_hypothesis = 5

# the hypothesis refers to the driving time mentioned in the premise
if robert_drive_premise <= robert_drive_hypothesis:
    # check if the estimate of 'robert_drive_hypothesis' contradicts the driving time reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the driving time
    # any increase in the driving time is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
