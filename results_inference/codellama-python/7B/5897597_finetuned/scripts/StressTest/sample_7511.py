drive_time_50mph_premise = 1
drive_time_50mph_hypothesis = 7
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at 50 mph and 60 mph from city A to city B mentioned in the premise
if drive_time_50mph_premise!= drive_time_50mph_hypothesis:
    # check if the driving time at 50 mph in the hypothesis contradicts the driving time at 50 mph reported in the premise
    label = "contradiction"
elif drive_time_60mph_premise!= drive_time_60mph_hypothesis:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
