# Premise: Yesterday it took Robert 4 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert more than 1 hours to drive from City A to City B.
# Golden Label: entailment

drive_time_premise = 4
drive_time_hypothesis = 1

# the hypothesis refers to the drive time from City A to City B mentioned in the premise
if drive_time_premise <= drive_time_hypothesis:
    # check if the estimate in the hypothesis contradicts the drive time in the premise
    label = "contradiction"
else:
    # if the drive time in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

