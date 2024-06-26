drive_time_premise = 3
drive_time_hypothesis = 8

# the hypothesis refers to the time Robert took to drive from City A to City B, mentioned in the premise
if drive_time_premise > drive_time_hypothesis:
    # check if 'drive_time_premise' contradicts the estimated drive time in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
