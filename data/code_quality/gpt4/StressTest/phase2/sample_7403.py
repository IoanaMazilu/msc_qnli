drive_time_46mph_premise = 1
drive_time_46mph_hypothesis = 3
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the same driving times at given speeds as the premise
if drive_time_46mph_hypothesis != drive_time_46mph_premise:
    # check if the driving time at 46mph in the hypothesis contradicts the driving time at the same speed in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at the same speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
