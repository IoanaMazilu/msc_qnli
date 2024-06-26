drive_time_premise = 6
drive_time_hypothesis = 7

# the hypothesis refers to the driving time from City A to City B mentioned in the premise
if drive_time_premise >= drive_time_hypothesis:
    # check if the estimate of 'drive_time_hypothesis' contradicts the driving time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
