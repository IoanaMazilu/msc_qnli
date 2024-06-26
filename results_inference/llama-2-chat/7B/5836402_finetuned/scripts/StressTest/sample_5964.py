drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis refers to the time taken by Robert to drive from City A to City B mentioned in the premise
if drive_time_premise >= drive_time_hypothesis:
    # check if the estimate of 'drive_time_hypothesis' contradicts the time taken by Robert in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
