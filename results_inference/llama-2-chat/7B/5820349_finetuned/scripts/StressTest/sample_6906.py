drive_time_44mph_premise = 1
drive_time_44mph_hypothesis = 2
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the drive times at 44mph and 60mph mentioned in the premise
if drive_time_44mph_premise >= drive_time_44mph_hypothesis:
    # check if the estimate of 'drive_time_44mph_hypothesis' contradicts the drive time at 44mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the drive time at 60mph in the hypothesis contradicts the drive time at 60mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
