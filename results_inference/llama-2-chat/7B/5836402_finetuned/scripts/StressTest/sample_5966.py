drive_time_premise = 4
drive_time_hypothesis = 5

# the hypothesis talks about the drive time from City A to City B, referenced also in the premise
if drive_time_hypothesis!= drive_time_premise:
    # check if the drive time in the hypothesis contradicts the drive time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
