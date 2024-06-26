drive_time_premise = 4
drive_time_hypothesis = 3

# the hypothesis refers to the time Robert took to drive from City A to City B mentioned in the premise
if drive_time_premise != drive_time_hypothesis:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
