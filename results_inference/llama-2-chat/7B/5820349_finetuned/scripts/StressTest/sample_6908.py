drive_time_44mph_premise = 1
drive_time_44mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the drive times at 44 mph and 60 mph from city A to city B mentioned in the premise
if drive_time_44mph_hypothesis >= drive_time_44mph_premise:
    # check if the estimate of 'drive_time_44mph_hypothesis' contradicts the drive time at 44 mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
