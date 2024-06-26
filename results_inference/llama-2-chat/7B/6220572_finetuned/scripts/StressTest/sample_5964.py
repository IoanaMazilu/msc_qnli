hours_drive_premise = 4
hours_drive_hypothesis = 8

# the hypothesis refers to the time taken to drive from City A to City B mentioned in the premise
if hours_drive_premise >= hours_drive_hypothesis:
    # check if the estimate of 'hours_drive_hypothesis' contradicts the time taken in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
