drive_time_42mph_premise = 1
drive_time_42mph_hypothesis = 7
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis talks about the driving time at 42 mph and 60 mph, referenced also in the premise
if drive_time_42mph_hypothesis!= drive_time_42mph_premise:
    # check if the driving time at 42 mph in the hypothesis contradicts the driving time at 42 mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)