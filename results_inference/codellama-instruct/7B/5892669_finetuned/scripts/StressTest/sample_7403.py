drive_time_46mph_premise = 1
drive_time_46mph_hypothesis = 3
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at 46 mph and 60 mph mentioned in the premise
if drive_time_46mph_premise!= drive_time_46mph_hypothesis:
    # check if the driving time at 46 mph in the hypothesis contradicts the driving time at 46 mph reported in the premise
    label = "contradiction"
elif drive_time_60mph_premise!= drive_time_60mph_hypothesis:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
