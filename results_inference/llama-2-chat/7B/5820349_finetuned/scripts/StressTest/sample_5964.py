drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis refers to the time it took Robert to drive from City A to City B mentioned in the premise
if drive_time_premise >= drive_time_hypothesis:
    # check if the time it took Robert to drive in the premise contradicts the estimate of less than 'drive_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
