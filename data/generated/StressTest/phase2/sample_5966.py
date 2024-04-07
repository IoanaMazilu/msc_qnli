# Premise: Yesterday it took Robert 4 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert 5 hours to drive from City A to City B.
# Golden Label: contradiction

drive_time_premise = 4
drive_time_hypothesis = 5

# the hypothesis refers to the driving time between two cities mentioned in the premise
if drive_time_hypothesis != drive_time_premise:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
else:
    # if the driving time in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

