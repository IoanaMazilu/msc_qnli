robert_drive_premise = 4
robert_drive_hypothesis = 8

# the hypothesis refers to the time taken to drive from City A to City B, mentioned in the premise
if robert_drive_premise <= robert_drive_hypothesis:
    # check if the estimate of 'robert_drive_hypothesis' contradicts the time taken to drive in the premise
    label = "contradiction"
else:
    # the premise gives a specific time taken, while the hypothesis gives a less specific estimate
    # any time taken less than 8 hours is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
