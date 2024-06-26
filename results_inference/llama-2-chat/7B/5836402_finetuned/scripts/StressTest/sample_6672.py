drive_time_premise = 1
drive_time_hypothesis = 5
speed_premise = 40
speed_hypothesis = 40

# the hypothesis refers to the total drive time and speed mentioned in the premise
if drive_time_premise >= drive_time_hypothesis:
    # check if the estimate of 'drive_time_hypothesis' contradicts the total drive time in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
