drive_time_44mph_premise = 1
drive_time_44mph_hypothesis = 2
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds from the premise
if drive_time_44mph_premise >= drive_time_44mph_hypothesis:
    # check if the estimate of 'drive_time_44mph_hypothesis' contradicts the driving time at 44 mph in the premise
    label = "contradiction"
elif drive_time_60mph_premise!= drive_time_60mph_hypothesis:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
