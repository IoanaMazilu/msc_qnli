# Premise: Yesterday it took Robert 6 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert 2 hours to drive from City A to City B.
# Golden Label: contradiction

drive_time_premise = 6
drive_time_hypothesis = 2

# the hypothesis refers to the driving time from City A to City B mentioned in the premise
if drive_time_premise != drive_time_hypothesis:
    # check if the drive time in the hypothesis contradicts the drive time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

