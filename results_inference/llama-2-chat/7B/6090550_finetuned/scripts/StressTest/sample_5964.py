yesterday_drive_time_premise = 4
yesterday_drive_time_hypothesis = 8

# the hypothesis talks about the time Robert took to drive from City A to City B, which is also mentioned in the premise
if yesterday_drive_time_hypothesis!= yesterday_drive_time_premise:
    # check if the drive time in the hypothesis contradicts the drive time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
