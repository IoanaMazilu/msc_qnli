yesterday_drive_time_premise = 4
yesterday_drive_time_hypothesis = 5

# the hypothesis talks about the time Robert took to drive from City A to City B, which is also mentioned in the premise
if yesterday_drive_time_hypothesis!= yesterday_drive_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
