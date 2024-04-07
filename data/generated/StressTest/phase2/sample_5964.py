# Premise: Yesterday it took Robert 4 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert less than 8 hours to drive from City A to City B.
# Golden Label: entailment

drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis is referring to the same drive time from City A to City B as mentioned in the premise
if drive_time_hypothesis < drive_time_premise:
    # check if the 'drive_time_hypothesis' contradicts the drive time in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

