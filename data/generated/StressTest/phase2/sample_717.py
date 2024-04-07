# Premise: Yesterday it took Robert 3 hours to drive from City X to City Y.
# Hypothesis: Yesterday it took Robert more than 1 hours to drive from City X to City Y.
# Golden Label: entailment

drive_time_premise = 3
drive_time_hypothesis = 1

# the hypothesis refers to the driving time from City X to City Y mentioned in the premise
if drive_time_premise <= drive_time_hypothesis:
    # check if the estimated 'drive_time_hypothesis' contradicts the driving time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

