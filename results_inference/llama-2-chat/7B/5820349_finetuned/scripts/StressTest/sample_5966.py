drive_time_premise = 4
drive_time_hypothesis = 5

# the hypothesis refers to the time it took Robert to drive from City A to City B, mentioned in the premise
if drive_time_hypothesis!= drive_time_premise:
    # check if the drive time in the hypothesis contradicts the drive time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
