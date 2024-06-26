drive_time_premise = [8, 3]
drive_time_hypothesis = [1, 3]
speed_premise = 50
speed_hypothesis = 50

# the hypothesis refers to the driving time and speed mentioned in the premise
if drive_time_premise[0] <= drive_time_hypothesis[0]:
    # check if the estimate of 'drive_time_hypothesis[0]" contradicts the driving time in the premise
    label = "contradiction"
elif drive_time_premise[1]!= drive_time_hypothesis[1]:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
